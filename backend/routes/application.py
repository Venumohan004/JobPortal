from flask import Blueprint, request, jsonify, current_app
from threading import Thread

from models import db, User
from models.application import Application
from models.job import Job

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from utils.email import send_email

application_bp = Blueprint("application", __name__)


# =====================================
# Background Email Function
# =====================================

def send_application_email(
    app,
    recruiter_email,
    candidate_name,
    candidate_email,
    job_title
):
    with app.app_context():
        try:
            send_email(
                subject="New Job Application",
                recipients=[recruiter_email],
                body=f"""
Hello Recruiter,

A new candidate has applied for your job.

Candidate Name: {candidate_name}
Candidate Email: {candidate_email}

Job Title: {job_title}

Please login to your Job Portal account to review the application.

Thank you,
Job Portal Team
"""
            )
            print("Application email sent successfully")

        except Exception as e:
            print("Email Error:", e)


# =====================================
# Apply for Job
# =====================================

@application_bp.route("/jobs/<int:job_id>/apply", methods=["POST"])
@jwt_required()
def apply_job(job_id):

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
            "message": "Only candidates can apply for jobs."
        }), 403

    candidate_id = int(get_jwt_identity())

    job = db.session.get(Job, job_id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404

    existing_application = Application.query.filter_by(
        candidate_id=candidate_id,
        job_id=job_id
    ).first()

    if existing_application:
        return jsonify({
            "message": "You have already applied for this job."
        }), 400

    try:
        application = Application(
            candidate_id=candidate_id,
            job_id=job_id
        )

        db.session.add(application)
        db.session.commit()
        db.session.refresh(application)

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "message": "Failed to apply for job",
            "error": str(e)
        }), 500

    # Send email in background
    recruiter = db.session.get(User, job.created_by)
    candidate = db.session.get(User, candidate_id)

    if recruiter and candidate:
        app = current_app._get_current_object()

        Thread(
            target=send_application_email,
            args=(
                app,
                recruiter.email,
                candidate.full_name,
                candidate.email,
                job.title
            )
        ).start()

    return jsonify({
        "message": "Job Applied Successfully",
        "application": application.to_dict()
    }), 201


# =====================================
# Get Applications
# Candidate -> own applications
# Recruiter/Admin -> all applications
# =====================================

@application_bp.route("/applications", methods=["GET"])
@jwt_required()
def get_applications():

    claims = get_jwt()
    user_id = int(get_jwt_identity())

    # Candidate: only own applications
    if claims["role"] == "candidate":

        applications = Application.query.filter_by(
            candidate_id=user_id
        ).all()

        result = []

        for app in applications:
            job = db.session.get(Job, app.job_id)

            if job:
                result.append({
                    "id": app.id,
                    "job_id": job.id,
                    "job_title": job.title,
                    "company": job.company,
                    "location": job.location,
                    "status": app.status if hasattr(app, "status") else "Applied"
                })

        return jsonify(result), 200

    # Recruiter/Admin: all applications
    elif claims["role"] in ["recruiter", "admin"]:

        applications = Application.query.all()

        return jsonify({
            "count": len(applications),
            "applications": [a.to_dict() for a in applications]
        }), 200

    return jsonify({
        "message": "Access denied"
    }), 403


# =====================================
# Delete Application
# =====================================

@application_bp.route("/applications/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_application(id):

    claims = get_jwt()
    user_id = int(get_jwt_identity())

    application = db.session.get(Application, id)

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


# =====================================
# Get Applications for a Recruiter's Job
# =====================================

@application_bp.route("/jobs/<int:job_id>/applications", methods=["GET"])
@jwt_required()
def get_job_applications(job_id):

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can view job applications"
        }), 403

    recruiter_id = int(get_jwt_identity())

    job = db.session.get(Job, job_id)

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
        "applications": [a.to_dict() for a in applications]
    }), 200


# =====================================
# Update Application Status
# =====================================

@application_bp.route("/applications/<int:id>/status", methods=["PUT"])
@jwt_required()
def update_application_status(id):

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can update application status"
        }), 403

    application = db.session.get(Application, id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    job = db.session.get(Job, application.job_id)

    if job.created_by != int(get_jwt_identity()):
        return jsonify({
            "message": "You can update only applications for your own jobs"
        }), 403

    data = request.get_json()

    if not data or "status" not in data:
        return jsonify({
            "message": "Status is required"
        }), 400

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

    try:
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "message": "Failed to update application status",
            "error": str(e)
        }), 500

    candidate = db.session.get(User, application.candidate_id)

    # Send status update email
    try:
        send_email(
            subject="Application Status Updated",
            recipients=[candidate.email],
            body=f"""
Hello {candidate.full_name},

Your application status has been updated.

Job Title: {job.title}

Current Status: {application.status}

Please log in to your Job Portal account to view more details.

Best Regards,
Job Portal Team
"""
        )
        print("Status update email sent successfully")

    except Exception as e:
        print("Status Email Error:", e)

    return jsonify({
        "message": "Application status updated successfully",
        "application": application.to_dict()
    }), 200