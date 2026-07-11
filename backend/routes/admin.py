from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.user import User
from models.job import Job
from models.application import Application
from models.candidate import Candidate
from models.recruiter import Recruiter
from sqlalchemy import func
from datetime import datetime, timedelta

admin_bp = Blueprint("admin", __name__)


# ==========================
# Get All Users
# ==========================
@admin_bp.route("/admin/users", methods=["GET"])
@jwt_required()
def get_users():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    users = User.query.all()

    return jsonify({
        "count": len(users),
        "users": [
            {
                "id": user.id,
                "email": user.email,
                "role": user.role
            }
            for user in users
        ]
    }), 200


# ==========================
# Delete User
# ==========================
@admin_bp.route("/admin/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.role == "admin":
        return jsonify({"message": "Admin account cannot be deleted"}), 400

    # Delete candidate applications
    Application.query.filter_by(candidate_id=user.id).delete()

    # Delete candidate profile
    Candidate.query.filter_by(user_id=user.id).delete()

    # Delete recruiter's jobs and their applications
    jobs = Job.query.filter_by(created_by=user.id).all()

    for job in jobs:
        Application.query.filter_by(job_id=job.id).delete()

    Job.query.filter_by(created_by=user.id).delete()

    # Delete recruiter profile
    Recruiter.query.filter_by(user_id=user.id).delete()

    # Delete user
    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "User deleted successfully"
    }), 200

# ==========================
# Admin Dashboard
# ==========================
@admin_bp.route("/admin/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin:
        return jsonify({"message": "User not found"}), 404

    if admin.role != "admin":
        return jsonify({"message": "Access denied"}), 403

    # Statistics
    total_users = User.query.count()
    total_recruiters = User.query.filter_by(role="recruiter").count()
    total_candidates = User.query.filter_by(role="candidate").count()
    total_jobs = Job.query.count()
    total_applications = Application.query.count()

    pending = Application.query.filter_by(status="Pending").count()
    accepted = Application.query.filter_by(status="Accepted").count()
    rejected = Application.query.filter_by(status="Rejected").count()

    # Latest Users
    latest_users = User.query.order_by(User.id.desc()).limit(5).all()

    users = []

    for user in latest_users:
        users.append({
            "id": user.id,
            "full_name": user.full_name, # Replace with user.username if needed
            "email": user.email,
            "role": user.role
        })

    # Latest Jobs
    latest_jobs = Job.query.order_by(Job.id.desc()).limit(5).all()

    jobs = []

    for job in latest_jobs:
        jobs.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location
        })

    # Latest Applications
    latest_applications = Application.query.order_by(Application.id.desc()).limit(5).all()

    applications = []

    for application in latest_applications:
        applications.append({
            "id": application.id,
            "candidate_id": application.candidate_id,
            "job_id": application.job_id,
            "status": application.status
        })

    return jsonify({

        "statistics": {
            "total_users": total_users,
            "total_recruiters": total_recruiters,
            "total_candidates": total_candidates,
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "pending": pending,
            "accepted": accepted,
            "rejected": rejected
        },

        "latest_users": users,

        "latest_jobs": jobs,

        "latest_applications": applications

    }), 200

# ==========================
# Application Status Report
# ==========================
@admin_bp.route("/admin/reports/applications", methods=["GET"])
@jwt_required()
def application_report():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    report = (
        db.session.query(
            Application.status,
            func.count(Application.id)
        )
        .group_by(Application.status)
        .all()
    )

    data = {}

    for status, count in report:
        data[status] = count

    return jsonify(data), 200

# ==========================
# Jobs Posted Per Recruiter
# ==========================
@admin_bp.route("/admin/reports/recruiters", methods=["GET"])
@jwt_required()
def recruiter_report():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    report = (
        db.session.query(
            Recruiter.company_name,
            func.count(Job.id).label("jobs_posted")
        )
        .join(Job, Recruiter.user_id == Job.created_by)
        .group_by(Recruiter.company_name)
        .all()
    )

    data = []

    for company, jobs in report:
        data.append({
            "company": company,
            "jobs_posted": jobs
        })

    return jsonify(data), 200

# ==========================
# Top Recruiters
# ==========================
@admin_bp.route("/admin/reports/top-recruiters", methods=["GET"])
@jwt_required()
def top_recruiters():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    report = (
        db.session.query(
            Recruiter.company_name,
            func.count(Job.id).label("jobs")
        )
        .join(Job, Recruiter.user_id == Job.created_by)
        .group_by(Recruiter.company_name)
        .order_by(func.count(Job.id).desc())
        .limit(5)
        .all()
    )

    data = []

    for company, jobs in report:
        data.append({
            "company": company,
            "jobs": jobs
        })

    return jsonify(data), 200

# ==========================
# Most Applied Jobs
# ==========================
@admin_bp.route("/admin/reports/top-jobs", methods=["GET"])
@jwt_required()
def top_jobs():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    report = (
        db.session.query(
            Job.title,
            func.count(Application.id).label("applications")
        )
        .join(Application, Job.id == Application.job_id)
        .group_by(Job.title)
        .order_by(func.count(Application.id).desc())
        .limit(5)
        .all()
    )

    data = []

    for title, applications in report:
        data.append({
            "job": title,
            "applications": applications
        })

    return jsonify(data), 200

# ==========================
# Candidate Registration Report
# ==========================
@admin_bp.route("/admin/reports/candidates", methods=["GET"])
@jwt_required()
def candidate_report():

    admin_id = int(get_jwt_identity())
    admin = db.session.get(User, admin_id)

    if not admin or admin.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    now = datetime.utcnow()

    today_start = datetime(now.year, now.month, now.day)
    week_start = now - timedelta(days=7)
    month_start = now - timedelta(days=30)

    today = User.query.filter(
        User.role == "candidate",
        User.created_at >= today_start
    ).count()

    this_week = User.query.filter(
        User.role == "candidate",
        User.created_at >= week_start
    ).count()

    this_month = User.query.filter(
        User.role == "candidate",
        User.created_at >= month_start
    ).count()

    return jsonify({
        "today": today,
        "this_week": this_week,
        "this_month": this_month
    }), 200