from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
import logging

from models import db
from models.candidate import Candidate
from models.application import Application
from models.saved_job import SavedJob
from models.job import Job
from models.recently_viewed_job import RecentlyViewedJob

candidate = Blueprint("candidate", __name__)

# ===========================
# Create Candidate Profile
# ===========================
@candidate.route("/candidate/profile", methods=["POST"])
@jwt_required()
def create_profile():

    user_id = int(get_jwt_identity())

    existing = Candidate.query.filter_by(user_id=user_id).first()

    if existing:
        return jsonify({
            "message": "Profile already exists"
        }), 400

    data = request.get_json()

    if not data:
        return jsonify({
        "message":"JSON required"
        }),400
    profile = Candidate(
        user_id=user_id,
        skills=data.get("skills"),
        education=data.get("education"),
        experience=data.get("experience"),
        address=data.get("address"),
        about=data.get("about"),
        location=data.get("location")
    )

    db.session.add(profile)
    db.session.commit()

    return jsonify({
        "message": "Candidate Profile Created Successfully"
    }), 201


# ===========================
# Get Candidate Profile
# ===========================
@candidate.route("/candidate/profile", methods=["GET"])
@jwt_required()
def get_profile():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
    }),403

    user_id = int(get_jwt_identity())

    profile = Candidate.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    return jsonify(profile.to_dict()), 200


# ===========================
# Update Candidate Profile
# ===========================
@candidate.route("/candidate/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
    }),403

    user_id = int(get_jwt_identity())

    profile = Candidate.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "message":"JSON required"
         }),400

    profile.skills = data.get("skills", profile.skills)
    profile.education = data.get("education", profile.education)
    profile.experience = data.get("experience", profile.experience)
    profile.address = data.get("address", profile.address)
    profile.about = data.get("about", profile.about)
    profile.location = data.get("location", profile.location)

    db.session.commit()

    return jsonify({
        "message": "Candidate profile updated successfully"
    }), 200


# ===========================
# Candidate Dashboard
# ===========================
@candidate.route("/candidate/dashboard", methods=["GET"])
@jwt_required()
def candidate_dashboard():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
    }),403
    user_id = int(get_jwt_identity())

    logging.info(
    f"Dashboard accessed by {user_id}"
    )

    applied_jobs = Application.query.filter_by(
        candidate_id=user_id
    ).count()

    saved_jobs = SavedJob.query.filter_by(
        candidate_id=user_id
    ).count()

    return jsonify({
        "applied_jobs": applied_jobs,
        "saved_jobs": saved_jobs
        }), 200


# ===========================
# Recent Applications
# ===========================
@candidate.route("/candidate/recent-applications", methods=["GET"])
@jwt_required()
def recent_applications():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
        }),403

    user_id = int(get_jwt_identity())

    applications = (
        Application.query
        .filter_by(candidate_id=user_id)
        .order_by(Application.created_at.desc())
        .limit(5)
        .all()
    )

    return jsonify({
        "count": len(applications),
        "applications": [
            application.to_dict()
            for application in applications
        ]
    }), 200


# ===========================
# Application Status
# ===========================
@candidate.route("/candidate/application-status", methods=["GET"])
@jwt_required()
def application_status():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
        }),403

    user_id = int(get_jwt_identity())

    logging.info(
    f"Application status accessed by {user_id}"
    )

    applied = Application.query.filter_by(
        candidate_id=user_id,
        status="Applied"
    ).count()

    shortlisted = Application.query.filter_by(
        candidate_id=user_id,
        status="Shortlisted"
    ).count()

    selected = Application.query.filter_by(
        candidate_id=user_id,
        status="Selected"
    ).count()

    rejected = Application.query.filter_by(
        candidate_id=user_id,
        status="Rejected"
    ).count()

    return jsonify({
        "applied": applied,
        "shortlisted": shortlisted,
        "selected": selected,
        "rejected": rejected
    }), 200


# ===========================
# Saved Jobs
# ===========================
@candidate.route("/candidate/saved-jobs", methods=["GET"])
@jwt_required()
def get_saved_jobs():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
        }),403

    user_id = int(get_jwt_identity())

    jobs = (
        db.session.query(Job)
        .join(SavedJob, Job.id == SavedJob.job_id)
        .filter(SavedJob.candidate_id == user_id)
        .order_by(Job.created_at.desc())
        .all()
    )

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200


# ===========================
# Recently Viewed Jobs
# ===========================
@candidate.route("/candidate/recent-jobs", methods=["GET"])
@jwt_required()
def recent_jobs():
    claims=get_jwt()

    if claims["role"]!="candidate":
        return jsonify({
            "message":"Only candidates allowed"
        }),403

    user_id = int(get_jwt_identity())

    viewed_jobs = (
        RecentlyViewedJob.query
        .filter_by(candidate_id=user_id)
        .order_by(RecentlyViewedJob.id.desc())
        .limit(5)
        .all()
    )

    jobs = []

    for viewed in viewed_jobs:
        job = db.session.get(Job, viewed.job_id)

        if job:
            jobs.append(job.to_dict())

    return jsonify({
        "count": len(jobs),
        "recent_jobs": jobs
    }), 200