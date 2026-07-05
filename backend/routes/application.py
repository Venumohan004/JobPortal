from flask import Blueprint, request, jsonify
from models import db
from models.application import Application

application_bp = Blueprint("application", __name__)

@application_bp.route("/apply", methods=["POST"])
def apply_job():
    data = request.get_json()

    application = Application(
        candidate_id=data["candidate_id"],
        job_id=data["job_id"]
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "message": "Job Applied Successfully",
        "application": application.to_dict()
    }), 201

@application_bp.route("/applications", methods=["GET"])
def get_applications():
    applications = Application.query.all()

    return jsonify({
        "count": len(applications),
        "applications": [application.to_dict() for application in applications]
    }), 200

@application_bp.route("/applications/<int:id>", methods=["DELETE"])
def delete_application(id):
    application = Application.query.get(id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    db.session.delete(application)
    db.session.commit()

    return jsonify({
        "message": "Application Deleted Successfully"
    }), 200

@application_bp.route("/jobs/<int:job_id>/applications", methods=["GET"])
def get_job_applications(job_id):
    applications = Application.query.filter_by(job_id=job_id).all()

    return jsonify({
        "job_id": job_id,
        "count": len(applications),
        "applications": [application.to_dict() for application in applications]
    }), 200