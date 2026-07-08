from flask import Blueprint
from models import User, Job, Application
from flask_jwt_extended import jwt_required
from utils.admin_required import admin_required
from models import db

admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@admin_required
def dashboard():

    return {
        "total_users": User.query.count(),
        "total_jobs": Job.query.count(),
        "total_applications": Application.query.count()
    }

@admin_bp.route("/users", methods=["GET"])
@jwt_required()
@admin_required
def all_users():

    users = User.query.all()

    result=[]

    for u in users:
        result.append({
            "id":u.id,
            "full_name":u.full_name,
            "email":u.email,
            "role":u.role,
            "created_at": str(u.created_at)
        })

    return {"users":result}

@admin_bp.route("/jobs", methods=["GET"])
@jwt_required()
@admin_required
def all_jobs():

    jobs = Job.query.all()

    result=[]

    for job in jobs:
        result.append({
            "id":job.id,
            "title":job.title,
            "company":job.company,
            "location":job.location
        })

    return {"jobs":result}

@admin_bp.route("/applications", methods=["GET"])
@jwt_required()
@admin_required
def all_applications():

    apps = Application.query.all()

    result = []

    for app in apps:
        result.append({
            "id": app.id,
            "candidate_id": app.candidate_id,
            "job_id": app.job_id,
            "status": app.status
        })

    return {"applications": result}

@admin_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(id):

    user = User.query.get(id)

    if not user:
        return {"message":"User not found"},404

    db.session.delete(user)
    db.session.commit()

    return {"message":"User deleted successfully"}

@admin_bp.route("/jobs/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_job(id):

    job = Job.query.get(id)

    if not job:
        return {"message":"Job not found"},404

    db.session.delete(job)
    db.session.commit()

    return {"message":"Job deleted successfully"}