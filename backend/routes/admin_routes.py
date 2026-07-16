from flask import Blueprint
from flask_jwt_extended import jwt_required
from models import db, User, Job, Application, Candidate, Recruiter
from utils.admin_required import admin_required
from sqlalchemy.exc import SQLAlchemyError

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@admin_required
def dashboard():
    """Return overall statistics for the admin dashboard."""
    return {
        "total_users": User.query.count(),
        "total_candidates": User.query.filter_by(role="candidate").count(),
        "total_recruiters": User.query.filter_by(role="recruiter").count(),
        "total_jobs": Job.query.count(),
        "total_applications": Application.query.count(),
        "applied": Application.query.filter_by(status="Applied").count(),
        "shortlisted": Application.query.filter_by(status="Shortlisted").count(),
        "selected": Application.query.filter_by(status="Selected").count(),
        "rejected": Application.query.filter_by(status="Rejected").count()
    }

@admin_bp.route("/users", methods=["GET"])
@jwt_required()
@admin_required
def all_users():
    """Return all registered users."""
    users = User.query.all()

    return {
        "users": [user.to_dict() for user in users]
    }


@admin_bp.route("/jobs", methods=["GET"])
@jwt_required()
@admin_required
def all_jobs():
    """Return all posted jobs."""
    jobs = Job.query.all()

    return {
        "jobs": [job.to_dict() for job in jobs]
    }


@admin_bp.route("/applications", methods=["GET"])
@jwt_required()
@admin_required
def all_applications():
    """Return all job applications."""
    apps = Application.query.all()

    return {
        "applications": [app.to_dict() for app in apps]
    }


@admin_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(id):
    """Delete a user."""

    user = db.session.get(User, id)

    if not user:
        return {"message": "User not found"}, 404

    if user.role == "admin":
        return {"message": "Admin account cannot be deleted"}, 400

    try:
        Application.query.filter_by(candidate_id=user.id).delete()

        Candidate.query.filter_by(user_id=user.id).delete()

        jobs = Job.query.filter_by(created_by=user.id).all()

        for job in jobs:
            Application.query.filter_by(job_id=job.id).delete()

        Job.query.filter_by(created_by=user.id).delete()

        Recruiter.query.filter_by(user_id=user.id).delete()

        db.session.delete(user)
        db.session.commit()

    except SQLAlchemyError:
        db.session.rollback()
        return {"message": "Failed to delete user"}, 500

    return {"message": "User deleted successfully"}

@admin_bp.route("/jobs/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_job(id):
    """Delete a job."""

    job = db.session.get(Job, id)

    if not job:
        return {"message": "Job not found"}, 404

    try:
        Application.query.filter_by(job_id=job.id).delete()

        db.session.delete(job)
        db.session.commit()

    except SQLAlchemyError:
        db.session.rollback()
        return {"message": "Failed to delete job"}, 500

    return {"message": "Job deleted successfully"}