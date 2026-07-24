from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
import traceback
from models import db, Interview, Application, Candidate, Job, User
from utils.recruiter_required import recruiter_required
from utils.email_utils import send_interview_email

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

        # Get application
        application = db.session.get(Application, application_id)

        if application is None:
            return jsonify({"message": "Application not found"}), 404

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

        print("Application status type:", type(application.status))
        print("Allowed enums:", Application.status.type.enums)
        print("Setting status to:", repr("Interview Scheduled"))

        # Update application status
        application.status = "Interview Scheduled"
        print("Before commit:", application.status)
        # Save to database first
        db.session.commit()

        # =====================================
        # Prepare email data
        # =====================================

        candidate = Candidate.query.filter_by(
            user_id=application.candidate_id
        ).first()

        if candidate is None:
            return jsonify({"message": "Candidate not found"}), 404

        user = db.session.get(User, candidate.user_id)

        if user is None:
            return jsonify({"message": "Candidate user account not found"}), 404

        job = db.session.get(Job, application.job_id)

        if job is None:
            return jsonify({"message": "Job not found"}), 404

        # Create interview_data dictionary
        interview_data = {
            "job_title": job.title,
            "company_name": job.company,   # <-- change this
            "interview_date": interview.interview_date,
            "interview_time": interview.interview_time,
            "mode": interview.mode,
            "meeting_link": interview.meeting_link,
            "location": interview.location
        }

        # Send email (do not fail API if email fails)
        email_sent = send_interview_email(
            candidate_email=user.email,
            candidate_name=user.full_name,   # use user.username if your model uses username
            interview_data=interview_data
        )

        return jsonify({
            "message": "Interview scheduled successfully",
            "email_sent": email_sent,
            "interview": interview.to_dict()
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        traceback.print_exc()

        return jsonify({
            "message": str(e)
        }), 500
       

    except Exception as e:
        db.session.rollback()
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

        interview.interview_date = data.get(
            "interview_date",
            interview.interview_date
        )

        interview.interview_time = data.get(
            "interview_time",
            interview.interview_time
        )

        interview.mode = data.get(
            "mode",
            interview.mode
        )

        interview.meeting_link = data.get(
            "meeting_link",
            interview.meeting_link
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
        return jsonify({"message": str(e)}), 500