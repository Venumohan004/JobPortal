from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from models import db
from models.recruiter import Recruiter
from models.user import User
from models.job import Job
from models.application import Application
from services.recommendation import calculate_match
from models.candidate import Candidate

recruiter_bp = Blueprint("recruiter", __name__)
 
@recruiter_bp.route("/recruiter/profile", methods=["POST"])
@jwt_required()
def create_recruiter():
    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)

    if not user:
        return jsonify({
        "message": "User not found"
    }), 404

    if user.role != "recruiter":
        return jsonify({
        "message": "Access denied"
    }), 403

    existing = Recruiter.query.filter_by(user_id=user_id).first()

    if existing:
        return jsonify({
        "message": "Recruiter profile already exists"
    }), 400

    data = request.get_json()

    recruiter = Recruiter(
    company_name=data.get("company_name"),
    company_email=data.get("company_email"),
    company_location=data.get("company_location"),
    company_website=data.get("company_website"),
    user_id=user_id
    )

    db.session.add(recruiter)
    db.session.commit()

    return jsonify({
        "message": "Recruiter Profile Created",
        "recruiter": recruiter.to_dict()
    }), 201

@recruiter_bp.route("/recruiter/profile", methods=["GET"])
@jwt_required()
def get_recruiter_profile():

    user_id = int(get_jwt_identity())

    recruiter = Recruiter.query.filter_by(user_id=user_id).first()

    if not recruiter:
        return jsonify({
            "message": "Recruiter profile not found"
        }), 404

    return jsonify(recruiter.to_dict()), 200

@recruiter_bp.route("/recruiter/profile", methods=["PUT"])
@jwt_required()
def update_recruiter_profile():

    user_id = int(get_jwt_identity())

    recruiter = Recruiter.query.filter_by(user_id=user_id).first()

    if not recruiter:
        return jsonify({
            "message": "Recruiter profile not found"
        }), 404

    data = request.get_json()

    recruiter.company_name = data.get("company_name", recruiter.company_name)
    recruiter.company_email = data.get("company_email", recruiter.company_email)
    recruiter.company_location = data.get("company_location", recruiter.company_location)
    recruiter.company_website = data.get("company_website", recruiter.company_website)

    db.session.commit()

    return jsonify({
        "message": "Recruiter profile updated successfully",
        "recruiter": recruiter.to_dict()
    }), 200

@recruiter_bp.route("/recruiter/dashboard", methods=["GET"])
@jwt_required()
def recruiter_dashboard():

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can access dashboard"
        }), 403

    recruiter_id = int(get_jwt_identity())

    total_jobs = Job.query.filter_by(created_by=recruiter_id).count()

    job_ids = [
        job.id
        for job in Job.query.filter_by(created_by=recruiter_id).all()
    ]

    total_applications = Application.query.filter(
        Application.job_id.in_(job_ids)
    ).count()

    return jsonify({
        "total_jobs": total_jobs,
        "total_applications": total_applications
    }), 200

@recruiter_bp.route("/recruiter/jobs/applications", methods=["GET"])
@jwt_required()
def applications_per_job():

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can access"
        }), 403

    recruiter_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(created_by=recruiter_id).all()

    result = []

    for job in jobs:

        count = Application.query.filter_by(
            job_id=job.id
        ).count()

        result.append({
            "job_id": job.id,
            "title": job.title,
            "company": job.company,
            "applications": count
        })

    return jsonify(result), 200

@recruiter_bp.route("/recruiter/recent-jobs", methods=["GET"])
@jwt_required()
def recent_jobs():

    recruiter_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(
        created_by=recruiter_id
    ).order_by(Job.id.desc()).limit(5).all()

    return jsonify({
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@recruiter_bp.route("/recruiter/jobs/<int:job_id>/recommended-candidates", methods=["GET"])
@jwt_required()
def recommended_candidates(job_id):
    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404
    recruiter = Recruiter.query.filter_by(user_id=user.id).first()

    if not recruiter:
        return jsonify({"message": "Recruiter profile not found"}), 404
    job = Job.query.get(job_id)

    if not job:
        return jsonify({"message": "Job not found"}), 404 
    
    if job.created_by != user_id:
        return jsonify({"message": "Unauthorized"}), 403 
    
    candidates = Candidate.query.all()

    recommendations = []

    for candidate in candidates:

        score = calculate_match(job, candidate)

        recommendations.append({
        "candidate_id": candidate.id,
        "score": score
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )
    return jsonify({
            "recommended_candidates": recommendations
    }), 200