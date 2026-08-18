from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from models import db, Interview, Application
from utils.recruiter_required import recruiter_required
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
            return jsonify({
                "message": "Request body is required"
            }), 400

        application_id = data.get("application_id")
        interview_date = data.get("interview_date")
        interview_time = data.get("interview_time")
        mode = data.get("mode")
        meeting_link = data.get("meeting_link")
        location = data.get("location")
        notes = data.get("notes")

        if not all([
            application_id,
            interview_date,
            interview_time,
            mode
        ]):
            return jsonify({
                "message": (
                    "application_id, interview_date, "
                    "interview_time and mode are required."
                )
            }), 400

        # Parse date
        try:
            interview_date = datetime.strptime(
                interview_date,
                "%Y-%m-%d"
            ).date()

            interview_time = datetime.strptime(
                interview_time,
                "%H:%M"
            ).time()

        except ValueError:
            return jsonify({
                "message": "Invalid date or time format."
            }), 400

        # Validate mode
        mode = mode.strip()

        if mode.lower() == "online" and not meeting_link:
            return jsonify({
                "message": "Meeting link is required for online interviews."
            }), 400

        if mode.lower() == "offline" and not location:
            return jsonify({
                "message": "Location is required for offline interviews."
            }), 400

        # Get application
        application = db.session.get(
            Application,
            int(application_id)
        )

        if application is None:
            return jsonify({
                "message": "Application not found"
            }), 404

        # Check existing interview
        existing = Interview.query.filter_by(
            application_id=application.id
        ).first()

        if existing:
            return jsonify({
                "message": "Interview already scheduled for this application."
            }), 409

        # Create interview
        interview = Interview(
            application_id=application.id,
            interview_date=interview_date,
            interview_time=interview_time,
            mode=mode,
            meeting_link=meeting_link,
            location=location,
            notes=notes
        )

        db.session.add(interview)

        # Update application status
        application.status = "Interview Scheduled"

        # Save
        db.session.commit()

        current_app.logger.info(
            f"Interview scheduled for application {application.id}"
        )

        return jsonify({
            "message": "Interview scheduled successfully",
            "interview": interview.to_dict()
        }), 201

    except SQLAlchemyError as e:

        db.session.rollback()

        current_app.logger.exception(
            "Interview scheduling database error"
        )

        return jsonify({
            "message": "Database error while scheduling interview",
            "error": str(e)
        }), 500

    except Exception as e:

        db.session.rollback()

        current_app.logger.exception(
            "Interview scheduling error"
        )

        return jsonify({
            "message": "Failed to schedule interview",
            "error": str(e)
        }), 500


# =====================================
# Get All Interviews
# =====================================

@interview_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_interviews():

    interviews = Interview.query.all()

    return jsonify({
        "count": len(interviews),
        "interviews": [
            interview.to_dict()
            for interview in interviews
        ]
    }), 200


# =====================================
# Get Interview By ID
# =====================================

@interview_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_interview(id):

    interview = db.session.get(Interview, id)

    if interview is None:
        return jsonify({
            "message": "Interview not found"
        }), 404

    return jsonify(
        interview.to_dict()
    ), 200


# =====================================
# Update Interview
# =====================================

@interview_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@recruiter_required
def update_interview(id):

    try:

        interview = db.session.get(
            Interview,
            id
        )

        if interview is None:
            return jsonify({
                "message": "Interview not found"
            }), 404

        data = request.get_json()

        if not data:
            return jsonify({
                "message": "Request body is required"
            }), 400

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

        return jsonify({
            "message": str(e)
        }), 500

    except Exception as e:

        db.session.rollback()

        current_app.logger.exception(e)

        return jsonify({
            "message": str(e)
        }), 500


# =====================================
# Delete Interview
# =====================================

@interview_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@recruiter_required
def delete_interview(id):

    try:

        interview = db.session.get(
            Interview,
            id
        )

        if interview is None:
            return jsonify({
                "message": "Interview not found"
            }), 404

        db.session.delete(interview)

        db.session.commit()

        return jsonify({
            "message": "Interview deleted successfully"
        }), 200

    except SQLAlchemyError as e:

        db.session.rollback()

        return jsonify({
            "message": str(e)
        }), 500

    except Exception as e:

        db.session.rollback()

        current_app.logger.exception(e)

        return jsonify({
            "message": str(e)
        }), 500