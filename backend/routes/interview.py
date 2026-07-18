from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from models import db, Interview, Application
from utils.recruiter_required import recruiter_required

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

        if not all([application_id, interview_date, interview_time, mode]):
            return jsonify({
                "message": "application_id, interview_date, interview_time and mode are required."
            }), 400

        application = db.session.get(Application, application_id)

        if application is None:
            return jsonify({"message": "Application not found"}), 404

        interview = Interview(
            application_id=application_id,
            interview_date=interview_date,
            interview_time=interview_time,
            mode=mode,
            meeting_link=meeting_link
        )

        db.session.add(interview)
        db.session.commit()

        return jsonify({
            "message": "Interview scheduled successfully",
            "interview": interview.to_dict()
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

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