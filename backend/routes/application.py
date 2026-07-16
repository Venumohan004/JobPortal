from flask import Blueprint, request, jsonify
from models import db
from models.application import Application
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models.job import Job
from models import User
from utils.email import send_email

application_bp = Blueprint("application", __name__)

@application_bp.route("/jobs/<int:job_id>/apply", methods=["POST"])
@jwt_required()
def apply_job(job_id):

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
        "message": "Only candidates can apply for jobs."
    }), 403

    candidate_id = int(get_jwt_identity())

    job = Job.query.get(job_id)

    if not job:
        return jsonify({
        "message": "Job not found"
    }), 404
    print("JWT Candidate ID:", candidate_id)
    print("Job ID:", job_id)

    existing_application = Application.query.filter_by(
    candidate_id= candidate_id,
    job_id=job_id
    ).first()
    print("Existing Application:", existing_application)

    if existing_application:
       return jsonify({
        "message": "You have already applied for this job."
    }), 400

    application = Application(
        candidate_id=candidate_id,
        job_id=job_id
    )

    db.session.add(application)
    db.session.commit()

    job = Job.query.get(job_id)

    recruiter = User.query.get(job.created_by)

    candidate = User.query.get(candidate_id)

    send_email(
        subject="New Job Application",
        recipients=[recruiter.email],
        body=f"""
        Hello Recruiter,

        A new candidate has applied.

        Candidate:
        {candidate.full_name}

        Job:
        {job.title}

        Please login to review the application.
        """
        )

    return jsonify({
        "message": "Job Applied Successfully",
        "application": application.to_dict()
    }), 201

@application_bp.route("/applications", methods=["GET"])
@jwt_required()
def get_applications():

    claims = get_jwt()
    

    if claims["role"] not in ["recruiter", "admin"]:
        return jsonify({
        "message": "Access denied"
    }), 403

    applications = Application.query.all()

    return jsonify({
        "count": len(applications),
        "applications": [application.to_dict() for application in applications]
    }), 200

@application_bp.route("/applications/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_application(id):
    claims = get_jwt()
    user_id = int(get_jwt_identity())

    application = Application.query.get(id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    if claims["role"] != "admin" and application.candidate_id != user_id:
        return jsonify({
            "message": "Access denied"
        }), 403

    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Application Deleted Successfully"
    }), 200

@application_bp.route("/jobs/<int:job_id>/applications", methods=["GET"])
@jwt_required()
def get_job_applications(job_id):
    
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can view job applications"
        }), 403
    recruiter_id = int(get_jwt_identity())

    job = Job.query.get(job_id)

    if not job:
        return jsonify({
        "message": "Job not found"
    }), 404

    if job.created_by != recruiter_id:
        return jsonify({
        "message": "You can view applications only for your own jobs"
    }), 403

    applications = Application.query.filter_by(job_id=job_id).all()

    return jsonify({
        "job_id": job_id,
        "count": len(applications),
        "applications": [application.to_dict() for application in applications]
    }), 200

@application_bp.route("/applications/<int:id>/status", methods=["PUT"])
@jwt_required()
def update_application_status(id):

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can update application status"
        }), 403

    # First fetch application
    application = Application.query.get(id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    # Then fetch job
    job = Job.query.get(application.job_id)

    if job.created_by != int(get_jwt_identity()):
        return jsonify({
            "message": "You can update only applications for your own jobs"
        }), 403

    data = request.get_json()

    allowed_status = [
        "Applied",
        "Shortlisted",
        "Rejected",
        "Selected"
    ]

    if data["status"] not in allowed_status:
        return jsonify({
            "message": "Invalid status"
        }), 400

    application.status = data["status"]

    db.session.commit()

    candidate = User.query.get(application.candidate_id)

    job = Job.query.get(application.job_id)

    try:
        send_email(
            subject="Application Status Updated",
            recipients=[candidate.email],
            body=f"""
            Hello {candidate.full_name},

            Your application status has been updated.

            Job Title:
            {job.title}

            Current Status:
            {application.status}

            Please log in to your Job Portal account to view more details.

            Best Regards,
            Job Portal Team
            """
        )
    except Exception as e:
        print(f"Email sending failed: {e}")
        
    return jsonify({
            "message": "Application status updated successfully",
            "application": application.to_dict()
         }), 200
    