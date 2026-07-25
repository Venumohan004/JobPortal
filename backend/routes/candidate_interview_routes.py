from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback

from models import Candidate, Application, Interview
from utils.candidate_required import candidate_required

candidate_interview_bp = Blueprint(
    "candidate_interview",
    __name__,
    url_prefix="/candidate"
)


# ==========================================================
# Get All Interviews for Logged-in Candidate
# ==========================================================
@candidate_interview_bp.route("/interviews", methods=["GET"])
@jwt_required()
@candidate_required
def get_candidate_interviews():
    try:
        user_id = int(get_jwt_identity())

        candidate = Candidate.query.filter_by(
            user_id=user_id
        ).first()

        if candidate is None:
            return jsonify({
                "message": "Candidate profile not found"
            }), 404

        applications = Application.query.filter_by(
            candidate_id=user_id
        ).all()

        interview_list = []

        for application in applications:

            interviews = Interview.query.filter_by(
                application_id=application.id
            ).all()

            job = application.job

            for interview in interviews:

                interview_list.append({
                    "id": interview.id,
                    "job_title": job.title if job else None,
                    "company": job.company if job else None,
                    "interview_date": str(interview.interview_date) if interview.interview_date else None,
                    "interview_time": str(interview.interview_time) if interview.interview_time else None,
                    "mode": interview.mode,
                    "meeting_link": interview.meeting_link,
                    "location": interview.location,
                    "notes": interview.notes
                })

        return jsonify({
            "count": len(interview_list),
            "interviews": interview_list
        }), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e)
        }), 500


# ==========================================================
# Get Single Interview
# ==========================================================
@candidate_interview_bp.route("/interviews/<int:id>", methods=["GET"])
@jwt_required()
@candidate_required
def get_candidate_interview(id):
    try:
        user_id = int(get_jwt_identity())

        candidate = Candidate.query.filter_by(
            user_id=user_id
        ).first()

        if candidate is None:
            return jsonify({
                "message": "Candidate profile not found"
            }), 404

        interview = Interview.query.get(id)

        if interview is None:
            return jsonify({
                "message": "Interview not found"
            }), 404

        application = interview.application

        if application.candidate_id != user_id:
            return jsonify({
                "message": "Unauthorized access"
            }), 403

        job = application.job

        return jsonify({
            "id": interview.id,
            "job_title": job.title if job else None,
            "company": job.company if job else None,
            "interview_date": str(interview.interview_date) if interview.interview_date else None,
            "interview_time": str(interview.interview_time) if interview.interview_time else None,
            "mode": interview.mode,
            "meeting_link": interview.meeting_link,
            "location": interview.location,
            "notes": interview.notes
        }), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "message": str(e)
        }), 500