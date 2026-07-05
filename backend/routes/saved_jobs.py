from flask import Blueprint, request, jsonify
from models import db
from models.saved_job import SavedJob

saved_bp = Blueprint("saved", __name__)

@saved_bp.route("/save-job", methods=["POST"])
def save_job():
    data = request.get_json()

    # prevent duplicates
    existing = SavedJob.query.filter_by(
        candidate_id=data["candidate_id"],
        job_id=data["job_id"]
    ).first()

    if existing:
        return jsonify({"message": "Job already saved"}), 400

    saved = SavedJob(
        candidate_id=data["candidate_id"],
        job_id=data["job_id"]
    )

    db.session.add(saved)
    db.session.commit()

    return jsonify({"message": "Job saved successfully"}), 201

@saved_bp.route("/saved-jobs/<int:candidate_id>", methods=["GET"])
def get_saved_jobs(candidate_id):
    jobs = SavedJob.query.filter_by(candidate_id=candidate_id).all()

    return jsonify({
        "count": len(jobs),
        "saved_jobs": [
            {"job_id": j.job_id, "candidate_id": j.candidate_id}
            for j in jobs
        ]
    }), 200

@saved_bp.route("/saved-jobs/<int:id>", methods=["DELETE"])
def delete_saved_job(id):
    saved = SavedJob.query.get(id)

    if not saved:
        return jsonify({"message": "Not found"}), 404

    db.session.delete(saved)
    db.session.commit()

    return jsonify({"message": "Removed successfully"}), 200