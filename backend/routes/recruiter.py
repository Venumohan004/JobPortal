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
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters allowed"
        }),403

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
    if not data:
        return jsonify({
        "message":"JSON required"
        }),400
    required = [
        "company_name",
        "company_email"
        ]

    for field in required:
        if field not in data:
         return jsonify({
            "message":f"{field} is required"
        }),400

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

    claims=get_jwt()

    if claims["role"]!="recruiter":
        return jsonify({
        "message":"Only recruiters allowed"
    }),403

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

    claims=get_jwt()

    if claims["role"]!="recruiter":
        return jsonify({
        "message":"Only recruiters allowed"
    }),403

    user_id = int(get_jwt_identity())

    recruiter = Recruiter.query.filter_by(user_id=user_id).first()

    if not recruiter:
        return jsonify({
            "message": "Recruiter profile not found"
        }), 404

    data = request.get_json()
    if not data:
        return jsonify({
        "message":"JSON required"
        }),400

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

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters allowed"
        }),403

    recruiter_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(
        created_by=recruiter_id
    ).order_by(Job.id.desc()).limit(5).all()

    return jsonify({
        "jobs": [job.to_dict() for job in jobs]
    }), 200
    
@recruiter_bp.route("/recruiter/jobs/<int:job_id>/applications", methods=["GET"])
@jwt_required()
def recruiter_job_applications(job_id):
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters allowed"
        }),403

    user_id = int(get_jwt_identity())

    job = Job.query.get(job_id)

    if not job:
        return jsonify({"message": "Job not found"}), 404

    if job.created_by != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    applications = Application.query.filter_by(job_id=job_id).all()

    result = []

    for application in applications:
        result.append({
            "application_id": application.id,
            "candidate_id": application.candidate_id,
            "status": application.status
        })

    return jsonify(result), 200

@recruiter_bp.route("/recruiter/jobs/<int:job_id>/recommended-candidates", methods=["GET"])
@jwt_required()
def recommended_candidates(job_id):
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters allowed"
        }),403
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

@recruiter_bp.route("/recruiter/candidates", methods=["GET"])
@jwt_required()
def search_candidates():

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({"message": "Only recruiters can access"}), 403

    query = Candidate.query

    skill = request.args.get("skill")
    location = request.args.get("location")
    experience = request.args.get("experience")
    education = request.args.get("education")

    if skill:
        query = query.filter(Candidate.skills.ilike(f"%{skill}%"))

    if location:
        query = query.filter(Candidate.location.ilike(f"%{location}%"))

    if experience:
        query = query.filter(Candidate.experience.ilike(f"%{experience}%"))

    if education:
        query = query.filter(Candidate.education.ilike(f"%{education}%"))

    candidates = query.all()

    result = []

    for candidate in candidates:

        result.append({
                "id": candidate.id,
                "user_id": candidate.user_id,
                "skills": candidate.skills,
                "education": candidate.education,
                "experience": candidate.experience,
                "address": candidate.address,
                "about": candidate.about,
                "location": candidate.location
            })

    return jsonify(result), 200

@recruiter_bp.route("/recruiter/candidate/<int:candidate_id>", methods=["GET"])
@jwt_required()
def get_candidate(candidate_id):

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters allowed"
        }),403

    candidate = Candidate.query.get(candidate_id)

    if not candidate:
        return jsonify({"message": "Candidate not found"}), 404

    return jsonify(candidate.to_dict()), 200

@recruiter_bp.route("/recruiter/recent-applicants", methods=["GET"])
@jwt_required()
def recent_applicants():

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({"message": "Only recruiters can access"}), 403

    recruiter_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(created_by=recruiter_id).all()

    job_ids = [job.id for job in jobs]

    applications = (
        Application.query
        .filter(Application.job_id.in_(job_ids))
        .order_by(Application.id.desc())
        .limit(10)
        .all()
    )

    result = []

    for application in applications:

        candidate = Candidate.query.filter_by(
            user_id=application.candidate_id
        ).first()

        user = User.query.get(application.candidate_id)

        job = Job.query.get(application.job_id)

        result.append({
            "application_id": application.id,
            "candidate_id": application.candidate_id,
            "candidate_name": user.full_name if user else None,
            "candidate_email": user.email if user else None,
            "job_id": application.job_id,
            "job_title": job.title if job else None,
            "status": application.status
        })

    return jsonify({
        "count": len(result),
        "recent_applicants": result
    }), 200