from flask import Blueprint, request, jsonify
from models import db
from models.job import Job
 
jobs_bp = Blueprint("jobs", __name__)
@jobs_bp.route("/jobs", methods=["POST"])
def create_job():
    try:
        data = request.get_json()
        print("Received Data:", data)

        job = Job(
            title=data["title"],
            company=data["company"],
            location=data["location"],
            salary=data["salary"],
            description=data["description"],
            created_by=data["created_by"]
        )

        db.session.add(job)
        db.session.commit()

        return jsonify({
            "message": "Job Created Successfully",
            "job": job.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

@jobs_bp.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/<int:id>", methods=["PUT"])
def update_job(id):
    job = Job.query.get(id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404

    data = request.get_json()

    job.title = data["title"]
    job.company = data["company"]
    job.location = data["location"]
    job.salary = data["salary"]
    job.description = data["description"]
    job.created_by = data["created_by"]

    db.session.commit()

    return jsonify({
        "message": "Job Updated Successfully",
        "job": job.to_dict()
    }), 200

@jobs_bp.route("/jobs/<int:id>", methods=["DELETE"])
def delete_job(id):
    job = Job.query.get(id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404

    db.session.delete(job)
    db.session.commit()

    return jsonify({
        "message": "Job Deleted Successfully"
    }), 200