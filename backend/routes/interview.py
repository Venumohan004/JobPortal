from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from models import db, Interview, Application, Job, User
from utils.recruiter_required import recruiter_required
from utils.email_utils import send_interview_email
from datetime import datetime

interview_bp = Blueprint("interview", __name__)

# =====================================
# Schedule Interview
# =====================================
@interview_bp.route("/", methods=["POST"])
@jwt_required()
@recruiter_required
def schedule_interview():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Request body is required"}), 400

        application_id = data.get("application_id")
        interview_date = data.get("interview_date")
        interview_time = data.get("interview_time")
        mode = data.get("mode")
        meeting_link = data.get("meeting_link")
        location = data.get("location")

        if not all([application_id, interview_date, interview_time, mode]):
            return jsonify({
                "message": "application_id, interview_date, interview_time and mode are required."
            }), 400

        interview_date = datetime.strptime(
            interview_date,
            "%Y-%m-%d"
        ).date()

        interview_time = datetime.strptime(
            interview_time,
            "%H:%M"
        ).time()

        if mode.lower() == "online" and not meeting_link:
            return jsonify({
                "message": "Meeting link is required for online interviews."
            }), 400

        if mode.lower() == "offline" and not location:
            return jsonify({
                "message": "Location is required for offline interviews."
            }), 400

        # Get application
        application = db.session.get(Application, application_id)

        if application is None:
            return jsonify({"message": "Application not found"}), 404

        existing = Interview.query.filter_by(
            application_id=application.id
        ).first()

        if existing:
            return jsonify({
                "message": "Interview already scheduled for this application."
            }), 409

        # Create interview
        interview = Interview(
            application_id=application_id,
            interview_date=interview_date,
            interview_time=interview_time,
            mode=mode,
            meeting_link=meeting_link,
            location=location
        )

        db.session.add(interview)

        current_app.logger.info(
            f"Interview scheduled for application {application.id}"
        )

        # Update application status
        application.status = "Interview Scheduled"

        # Save to database first
        db.session.commit()

        # =====================================
        # Prepare email data
        # =====================================

        user = db.session.get(User, application.candidate_id)

        if user is None:
            return jsonify({
                "message": "Candidate user account not found"
            }), 404

        # Create interview_data dictionary
        job = db.session.get(Job, application.job_id)

        if job is None:
            return jsonify({
                "message": "Job not found"
            }), 404
        
        interview_data = {
            "job_title": job.title,
            "company_name": job.company,   # <-- change this
            "interview_date": interview.interview_date,
            "interview_time": interview.interview_time,
            "mode": interview.mode,
            "meeting_link": interview.meeting_link,
            "location": interview.location
        }

        # ==========================
        # Send Email (Optional)
        # ==========================

        email_sent = False

        try:
            email_sent = send_interview_email(
                candidate_email=user.email,
                candidate_name=user.full_name,
                interview_data=interview_data
            )
        except Exception as e:
            current_app.logger.error(f"Email failed: {str(e)}")
            email_sent = False

        return jsonify({
            "message": "Interview scheduled successfully",
            "email_sent": email_sent,
            "interview": interview.to_dict()
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        current_app.logger.exception(e)

        return jsonify({
            "message": str(e)
        }), 500
       

    except Exception as e:
        db.session.rollback()
        current_app.logger.exception(e)
        return jsonify({"message": str(e)}), 500
            
# =====================================
# Get All Interviews
# =====================================
@interview_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_interviews():

    interviews = Interview.query.all()

    return jsonify({
        "count": len(interviews),
        "interviews": [interview.to_dict() for interview in interviews]
    }), 200


# =====================================
# Get Interview By ID
# =====================================
@interview_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_interview(id):

    interview = db.session.get(Interview, id)

    if interview is None:
        return jsonify({"message": "Interview not found"}), 404

    return jsonify(interview.to_dict()), 200


# =====================================
# Update Interview
# =====================================
@interview_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@recruiter_required
def update_interview(id):
    try:

        interview = db.session.get(Interview, id)

        if interview is None:
            return jsonify({"message": "Interview not found"}), 404

        data = request.get_json()

        if not data:
            return jsonify({"message": "Request body is required"}), 400

        if data.get("interview_date"):
            interview.interview_date = datetime.strptime(
                data["interview_date"],
                "%Y-%m-%d"
            ).date()

        if data.get("interview_time"):
            interview.interview_time = datetime.strptime(
                data["interview_time"],
                "%H:%M"
            ).time()

        interview.mode = data.get(
            "mode",
            interview.mode
        )

        interview.meeting_link = data.get(
            "meeting_link",
            interview.meeting_link
        )
        interview.location = data.get(
            "location",
            interview.location
        )

        interview.notes = data.get(
            "notes",
            interview.notes
        )

        db.session.commit()

        return jsonify({
            "message": "Interview updated successfully",
            "interview": interview.to_dict()
        }), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    except Exception as e:
        db.session.rollback()
        current_app.logger.exception(e)
        return jsonify({"message": str(e)}), 500


# =====================================
# Delete Interview
# =====================================
@interview_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@recruiter_required
def delete_interview(id):
    try:

        interview = db.session.get(Interview, id)

        if interview is None:
            return jsonify({"message": "Interview not found"}), 404

        db.session.delete(interview)
        db.session.commit()

        return jsonify({
            "message": "Interview deleted successfully"
        }), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    except Exception as e:
        db.session.rollback()
        current_app.logger.exception(e)
        return jsonify({"message": str(e)}), 500