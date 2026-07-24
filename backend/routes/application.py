from flask import Blueprint, request, jsonify, current_app
from threading import Thread

from models import db, User
from models.application import Application
from models.job import Job
from models.interview import Interview

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from utils.email_utils import send_email
from models.application_status_history import ApplicationStatusHistory

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
# Candidate - My Applications
# =====================================

@application_bp.route("/my-applications", methods=["GET"])
@jwt_required()
def my_applications():

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
            "message": "Only candidates can view their applications"
        }), 403

    candidate_id = int(get_jwt_identity())

    applications = Application.query.filter_by(
        candidate_id=candidate_id
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
                "status": getattr(app, "status", "Applied"),
                "created_at": app.created_at.isoformat() if getattr(app, "created_at", None) else None
            })

    return jsonify({
        "count": len(result),
        "applications": result
    }), 200


# =====================================
# Get Applications (Recruiter/Admin)
# =====================================

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
        "applications": [a.to_dict() for a in applications]
    }), 200


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

    result = []

    for app in applications:
        result.append({
            "id": app.id,
            "candidate_id": app.candidate_id,
            "status": getattr(app, "status", "Applied"),
            "created_at": app.created_at.isoformat() if getattr(app, "created_at", None) else None
        })

    return jsonify(result), 200


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
        "Interview Scheduled",
        "Rejected",
        "Selected"
    ]

    if data["status"] not in allowed_status:
        return jsonify({
            "message": "Invalid status"
        }), 400

    old_status = application.status

    application.status = data["status"]

    history = ApplicationStatusHistory(
        application_id=application.id,
        old_status=old_status,
        new_status=application.status
    )

    try:
        db.session.add(history)
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

# =====================================
# Schedule Interview
# =====================================

@application_bp.route("/applications/<int:id>/schedule", methods=["POST"])
@jwt_required()
def schedule_interview(id):

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can schedule interviews"
        }), 403

    application = db.session.get(Application, id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    job = db.session.get(Job, application.job_id)

    if job.created_by != int(get_jwt_identity()):
        return jsonify({
            "message": "You can schedule interviews only for your own jobs"
        }), 403

    data = request.get_json()

    required_fields = [
        "interview_date",
        "interview_time",
        "mode"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    interview = Interview(
        application_id=application.id,
        interview_date=data["interview_date"],
        interview_time=data["interview_time"],
        mode=data["mode"],
        meeting_link=data.get("meeting_link"),
        location=data.get("location"),
        notes=data.get("notes")
    )
    
    print(Application.status.type.enums)
    application.status = "Interview Scheduled"

    try:
        db.session.add(interview)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "message": "Failed to schedule interview",
            "error": str(e)
        }), 500

    candidate = db.session.get(User, application.candidate_id)

    # Send interview email
    try:
        send_email(
            subject="Interview Scheduled",
            recipients=[candidate.email],
            body=f"""
Hello {candidate.full_name},

Your interview has been scheduled.

Job Title: {job.title}

Date: {interview.interview_date}
Time: {interview.interview_time}
Mode: {interview.mode}

Meeting Link: {interview.meeting_link or "N/A"}
Location: {interview.location or "N/A"}

Notes:
{interview.notes or "No additional notes"}

Best Regards,
Job Portal Team
"""
        )

    except Exception as e:
        print("Interview Email Error:", e)

    return jsonify({
        "message": "Interview scheduled successfully",
        "interview": interview.to_dict()
    }), 201

# =====================================
# Candidate - My Interviews
# =====================================

@application_bp.route("/my-interviews", methods=["GET"])
@jwt_required()
def my_interviews():

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
            "message": "Only candidates can view interviews"
        }), 403

    candidate_id = int(get_jwt_identity())

    applications = Application.query.filter_by(
        candidate_id=candidate_id
    ).all()

    result = []

    for app in applications:
        interviews = Interview.query.filter_by(
            application_id=app.id
        ).all()

        job = db.session.get(Job, app.job_id)

        for interview in interviews:
            result.append({
                "id": interview.id,
                "job_title": job.title if job else "N/A",
                "company": job.company if job else "N/A",
                "interview_date": interview.interview_date,
                "interview_time": interview.interview_time,
                "mode": interview.mode,
                "meeting_link": interview.meeting_link,
                "location": interview.location,
                "notes": interview.notes
            })

    return jsonify({
        "count": len(result),
        "interviews": result
    }), 200

# =====================================
# Get Application Status History
# =====================================

@application_bp.route("/applications/<int:id>/status-history", methods=["GET"])
@jwt_required()
def get_application_status_history(id):

    claims = get_jwt()

    if claims["role"] not in ["recruiter", "admin"]:
        return jsonify({
            "message": "Access denied"
        }), 403

    application = db.session.get(Application, id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    history = ApplicationStatusHistory.query.filter_by(
        application_id=id
    ).order_by(ApplicationStatusHistory.changed_at.asc()).all()

    return jsonify({
        "count": len(history),
        "history": [item.to_dict() for item in history]
    }), 200