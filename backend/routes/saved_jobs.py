import traceback
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.saved_job import SavedJob
from models.job import Job

saved_bp = Blueprint("saved", __name__)


# ==========================================================
# Save Job
# ==========================================================
@saved_bp.route("/save-job/<int:job_id>", methods=["POST"])
@jwt_required()
def save_job(job_id):
    try:

        candidate_id = get_jwt_identity()

        job = Job.query.get(job_id)

        if not job:
            return jsonify({
                "message": "Job not found"
            }), 404

        existing = SavedJob.query.filter_by(
            candidate_id=candidate_id,
            job_id=job_id
        ).first()

        if existing:
            return jsonify({
                "message": "Job already saved"
            }), 400

        saved_job = SavedJob(
            candidate_id=candidate_id,
            job_id=job_id
        )

        db.session.add(saved_job)
        db.session.commit()

        return jsonify({
            "message": "Job saved successfully",
            "saved_job": saved_job.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

        return jsonify({
            "message": "Internal Server Error",
            "error": str(e)
        }), 500


# ==========================================================
# Get Saved Jobs
# ==========================================================
@saved_bp.route("/saved-jobs", methods=["GET"])
@jwt_required()
def get_saved_jobs():

    candidate_id = get_jwt_identity()

    saved_jobs = SavedJob.query.filter_by(
        candidate_id=candidate_id
    ).all()

    return jsonify({
        "count": len(saved_jobs),
        "saved_jobs": [
            job.to_dict()
            for job in saved_jobs
        ]
    }), 200


# ==========================================================
# Delete Saved Job
# ==========================================================
@saved_bp.route("/saved-jobs/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_saved_job(id):

    try:

        candidate_id = get_jwt_identity()

        saved_job = SavedJob.query.filter_by(
            id=id,
            candidate_id=candidate_id
        ).first()

        if not saved_job:
            return jsonify({
                "message": "Saved job not found"
            }), 404

        db.session.delete(saved_job)
        db.session.commit()

        return jsonify({
            "message": "Saved job removed successfully"
        }), 200

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

        return jsonify({
            "message": "Internal Server Error",
            "error": str(e)
        }), 500