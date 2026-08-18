from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func
from datetime import datetime, timedelta

from models import db
from models.user import User
from models.job import Job
from models.application import Application
from models.candidate import Candidate
from models.recruiter import Recruiter
from models.resume import Resume
from models.saved_job import SavedJob
from models.interview import Interview


admin_bp = Blueprint("admin", __name__)


# ============================================================
# ADMIN AUTHORIZATION
# ============================================================

def get_current_admin():
    """Return the currently logged-in admin user."""

    try:
        user_id = int(get_jwt_identity())
    except (TypeError, ValueError):
        return None

    user = db.session.get(User, user_id)

    if not user or user.role != "admin":
        return None

    return user

# ============================================================
# ADMIN PROFILE - GET
# ============================================================

@admin_bp.route("/admin/profile", methods=["GET"])
@jwt_required()
def get_admin_profile():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    return jsonify({
        "id": admin.id,
        "full_name": admin.full_name,
        "email": admin.email,
        "role": admin.role
    }), 200


# ============================================================
# ADMIN PROFILE - UPDATE
# ============================================================

@admin_bp.route("/admin/profile", methods=["PUT"])
@jwt_required()
def update_admin_profile():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "JSON data is required"
        }), 400

    full_name = data.get("full_name")
    email = data.get("email")

    if not full_name:
        return jsonify({
            "message": "Admin name is required"
        }), 400

    if not email:
        return jsonify({
            "message": "Admin email is required"
        }), 400

    try:

        # Check whether another user already uses this email
        existing_user = User.query.filter(
            User.email == email,
            User.id != admin.id
        ).first()

        if existing_user:
            return jsonify({
                "message": "Email is already in use"
            }), 400

        admin.full_name = full_name
        admin.email = email

        db.session.commit()

        return jsonify({
            "message": "Admin profile updated successfully",
            "admin": {
                "id": admin.id,
                "full_name": admin.full_name,
                "email": admin.email,
                "role": admin.role
            }
        }), 200

    except Exception as e:

        db.session.rollback()

        print("ADMIN PROFILE UPDATE ERROR:", e)

        return jsonify({
            "message": "Failed to update admin profile",
            "error": str(e)
        }), 500
# ============================================================
# ADMIN DASHBOARD
# ============================================================

@admin_bp.route("/admin/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    total_users = User.query.count()
    total_recruiters = User.query.filter_by(
        role="recruiter"
    ).count()

    total_candidates = User.query.filter_by(
        role="candidate"
    ).count()

    total_jobs = Job.query.count()
    total_applications = Application.query.count()

    applied = Application.query.filter_by(
        status="Applied"
    ).count()

    shortlisted = Application.query.filter_by(
        status="Shortlisted"
    ).count()

    selected = Application.query.filter_by(
        status="Selected"
    ).count()

    rejected = Application.query.filter_by(
        status="Rejected"
    ).count()

    latest_users = User.query.order_by(
        User.id.desc()
    ).limit(5).all()

    latest_jobs = Job.query.order_by(
        Job.id.desc()
    ).limit(5).all()

    latest_applications = Application.query.order_by(
        Application.id.desc()
    ).limit(5).all()

    return jsonify({

        "statistics": {
            "total_users": total_users,
            "total_recruiters": total_recruiters,
            "total_candidates": total_candidates,
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "applied": applied,
            "shortlisted": shortlisted,
            "selected": selected,
            "rejected": rejected
        },

        "latest_users": [
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role
            }
            for user in latest_users
        ],

        "latest_jobs": [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "location": job.location
            }
            for job in latest_jobs
        ],

        "latest_applications": [
            {
                "id": application.id,
                "candidate_id": application.candidate_id,
                "job_id": application.job_id,
                "status": application.status
            }
            for application in latest_applications
        ]

    }), 200


# ============================================================
# GET ALL USERS
# ============================================================

@admin_bp.route("/admin/users", methods=["GET"])
@jwt_required()
def get_users():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    users = User.query.order_by(
        User.id.desc()
    ).all()

    return jsonify({
        "count": len(users),
        "users": [
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role
            }
            for user in users
        ]
    }), 200


# ============================================================
# DELETE USER
# ============================================================

@admin_bp.route("/admin/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    if user.role == "admin":
        return jsonify({
            "message": "Admin account cannot be deleted"
        }), 400

    try:

        # Delete candidate applications
        applications = Application.query.filter_by(
            candidate_id=user.id
        ).all()

        for application in applications:

            Interview.query.filter_by(
                application_id=application.id
            ).delete(
                synchronize_session=False
            )

        Application.query.filter_by(
            candidate_id=user.id
        ).delete(
            synchronize_session=False
        )

        # Saved jobs
        SavedJob.query.filter_by(
            candidate_id=user.id
        ).delete(
            synchronize_session=False
        )

        # Resumes
        Resume.query.filter_by(
            candidate_id=user.id
        ).delete(
            synchronize_session=False
        )

        # Candidate profile
        Candidate.query.filter_by(
            user_id=user.id
        ).delete(
            synchronize_session=False
        )

        # Jobs created by recruiter
        jobs = Job.query.filter_by(
            created_by=user.id
        ).all()

        for job in jobs:

            applications = Application.query.filter_by(
                job_id=job.id
            ).all()

            for application in applications:

                Interview.query.filter_by(
                    application_id=application.id
                ).delete(
                    synchronize_session=False
                )

            Application.query.filter_by(
                job_id=job.id
            ).delete(
                synchronize_session=False
            )

            SavedJob.query.filter_by(
                job_id=job.id
            ).delete(
                synchronize_session=False
            )

            db.session.delete(job)

        # Recruiter profile
        Recruiter.query.filter_by(
            user_id=user.id
        ).delete(
            synchronize_session=False
        )

        db.session.delete(user)

        db.session.commit()

        return jsonify({
            "message": "User deleted successfully"
        }), 200

    except Exception as e:

        db.session.rollback()

        print("DELETE USER ERROR:", e)

        return jsonify({
            "message": "Failed to delete user",
            "error": str(e)
        }), 500


# ============================================================
# GET ALL JOBS
# ============================================================

@admin_bp.route("/admin/jobs", methods=["GET"])
@jwt_required()
def get_all_jobs():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    jobs = Job.query.order_by(
        Job.id.desc()
    ).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [
            job.to_dict()
            for job in jobs
        ]
    }), 200


# ============================================================
# ADD JOB - ADMIN
# ============================================================

@admin_bp.route("/admin/jobs", methods=["POST"])
@jwt_required()
def add_job():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "JSON data is required"
        }), 400

    title = data.get("title")
    company = data.get("company")
    location = data.get("location")

    if not title:
        return jsonify({
            "message": "Job title is required"
        }), 400

    try:

        job = Job(
            title=title,
            company=company,
            location=location,
            min_salary=data.get("min_salary"),
            max_salary=data.get("max_salary"),
            description=data.get("description"),
            skills=data.get("skills"),
            experience=data.get("experience"),
            job_type=data.get("job_type"),

            # IMPORTANT:
            # The logged-in admin becomes the creator
            created_by=admin.id,

            created_at=datetime.utcnow()
        )

        db.session.add(job)
        db.session.commit()

        return jsonify({
            "message": "Job created successfully",
            "job": job.to_dict()
        }), 201

    except Exception as e:

        db.session.rollback()

        print("ADMIN ADD JOB ERROR:", e)

        return jsonify({
            "message": "Failed to create job",
            "error": str(e)
        }), 500


# ============================================================
# DELETE JOB
# ============================================================

@admin_bp.route("/admin/jobs/<int:job_id>", methods=["DELETE"])
@jwt_required()
def delete_job(job_id):

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    job = db.session.get(Job, job_id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404

    try:

        applications = Application.query.filter_by(
            job_id=job.id
        ).all()

        for application in applications:

            Interview.query.filter_by(
                application_id=application.id
            ).delete(
                synchronize_session=False
            )

        Application.query.filter_by(
            job_id=job.id
        ).delete(
            synchronize_session=False
        )

        SavedJob.query.filter_by(
            job_id=job.id
        ).delete(
            synchronize_session=False
        )

        db.session.delete(job)

        db.session.commit()

        return jsonify({
            "message": "Job deleted successfully"
        }), 200

    except Exception as e:

        db.session.rollback()

        print("ADMIN DELETE JOB ERROR:", e)

        return jsonify({
            "message": "Failed to delete job",
            "error": str(e)
        }), 500


# ============================================================
# GET ALL APPLICATIONS
# ============================================================

@admin_bp.route("/admin/applications", methods=["GET"])
@jwt_required()
def get_all_applications():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    applications = Application.query.order_by(
        Application.id.desc()
    ).all()

    return jsonify({
        "count": len(applications),
        "applications": [
            application.to_dict()
            for application in applications
        ]
    }), 200


# ============================================================
# DELETE APPLICATION
# ============================================================

@admin_bp.route(
    "/admin/applications/<int:application_id>",
    methods=["DELETE"]
)
@jwt_required()
def delete_application(application_id):

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    application = db.session.get(
        Application,
        application_id
    )

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    try:

        # Delete related interviews first
        Interview.query.filter_by(
            application_id=application.id
        ).delete(
            synchronize_session=False
        )

        db.session.delete(application)

        db.session.commit()

        return jsonify({
            "message": "Application deleted successfully"
        }), 200

    except Exception as e:

        db.session.rollback()

        print("ADMIN DELETE APPLICATION ERROR:", e)

        return jsonify({
            "message": "Failed to delete application",
            "error": str(e)
        }), 500


# ============================================================
# APPLICATION REPORT
# ============================================================

@admin_bp.route(
    "/admin/reports/applications",
    methods=["GET"]
)
@jwt_required()
def application_report():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    report = (
        db.session.query(
            Application.status,
            func.count(Application.id)
        )
        .group_by(Application.status)
        .all()
    )

    return jsonify({
        status: count
        for status, count in report
    }), 200


# ============================================================
# RECRUITER REPORT
# ============================================================

@admin_bp.route(
    "/admin/reports/recruiters",
    methods=["GET"]
)
@jwt_required()
def recruiter_report():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    report = (
        db.session.query(
            Recruiter.company_name,
            func.count(Job.id).label("jobs_posted")
        )
        .join(
            Job,
            Recruiter.user_id == Job.created_by
        )
        .group_by(
            Recruiter.company_name
        )
        .all()
    )

    return jsonify([
        {
            "company": company,
            "jobs_posted": jobs
        }
        for company, jobs in report
    ]), 200


# ============================================================
# TOP RECRUITERS
# ============================================================

@admin_bp.route(
    "/admin/reports/top-recruiters",
    methods=["GET"]
)
@jwt_required()
def top_recruiters():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    report = (
        db.session.query(
            Recruiter.company_name,
            func.count(Job.id).label("jobs")
        )
        .join(
            Job,
            Recruiter.user_id == Job.created_by
        )
        .group_by(
            Recruiter.company_name
        )
        .order_by(
            func.count(Job.id).desc()
        )
        .limit(5)
        .all()
    )

    return jsonify([
        {
            "company": company,
            "jobs": jobs
        }
        for company, jobs in report
    ]), 200


# ============================================================
# TOP JOBS
# ============================================================

@admin_bp.route(
    "/admin/reports/top-jobs",
    methods=["GET"]
)
@jwt_required()
def top_jobs():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    report = (
        db.session.query(
            Job.title,
            func.count(Application.id).label(
                "applications"
            )
        )
        .join(
            Application,
            Job.id == Application.job_id
        )
        .group_by(
            Job.title
        )
        .order_by(
            func.count(Application.id).desc()
        )
        .limit(5)
        .all()
    )

    return jsonify([
        {
            "job": title,
            "applications": applications
        }
        for title, applications in report
    ]), 200


# ============================================================
# CANDIDATE REGISTRATION REPORT
# ============================================================

@admin_bp.route(
    "/admin/reports/candidates",
    methods=["GET"]
)
@jwt_required()
def candidate_report():

    admin = get_current_admin()

    if not admin:
        return jsonify({
            "message": "Access denied"
        }), 403

    now = datetime.utcnow()

    today_start = datetime(
        now.year,
        now.month,
        now.day
    )

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
    
