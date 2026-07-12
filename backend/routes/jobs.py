from flask import Blueprint, request, jsonify
from models import db
from models.job import Job
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import or_
from models.saved_job import SavedJob
from models.recently_viewed_job import RecentlyViewedJob

jobs_bp = Blueprint("jobs", __name__)
@jobs_bp.route("/jobs", methods=["POST"])
@jwt_required()
def create_job():

    try:
        claims = get_jwt()

        if claims["role"] != "recruiter":
            return jsonify({
                "message": "Only recruiters can create jobs"
            }), 403
            
        data = request.get_json()

        job = Job(
            title=data["title"],
            company=data["company"],
            location=data["location"],
            salary=data["salary"],
            description=data["description"],
            skills=data.get("skills"),
            experience=data.get("experience"),
            created_by=int(get_jwt_identity())
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

    search = request.args.get("search")
    company = request.args.get("company")
    location = request.args.get("location")
    title = request.args.get("title", "")

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    min_salary = request.args.get("min_salary", type=int)
    max_salary = request.args.get("max_salary", type=int)

    sort = request.args.get("sort")

    query = Job.query

    if search:
        query = query.filter(
            or_(
                Job.title.ilike(f"%{search}%"),
                Job.company.ilike(f"%{search}%"),
                Job.location.ilike(f"%{search}%"),
                Job.description.ilike(f"%{search}%")
            )
        )

    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    if title:
        query = query.filter(Job.title.ilike(f"%{title}%"))

    if min_salary:
        query = query.filter(Job.salary >= min_salary)

    if max_salary:
        query = query.filter(Job.salary <= max_salary)

    if sort == "salary_asc":
        query = query.order_by(Job.salary.asc())

    elif sort == "salary_desc":
        query = query.order_by(Job.salary.desc())

    elif sort == "latest":
        query = query.order_by(Job.id.desc())

    elif sort == "oldest":
        query = query.order_by(Job.id.asc())

    elif sort == "title":
        query = query.order_by(Job.title.asc())

    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total_jobs": pagination.total,
        "total_pages": pagination.pages,
        "jobs": [job.to_dict() for job in pagination.items]
    }), 200

 
@jobs_bp.route("/jobs/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_job(id):
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can delete jobs"
        }), 403

    job = db.session.get(Job, id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404
    
    if job.created_by != int(get_jwt_identity()):
        return jsonify({
        "message": "You can delete only your own jobs"
    }), 403

    db.session.delete(job)
    db.session.commit()

    return jsonify({
        "message": "Job Deleted Successfully"
    }), 200

@jobs_bp.route("/jobs/search", methods=["GET"])
def search_jobs():

    search = request.args.get("search", "")

    jobs = Job.query.filter(
        or_(
            Job.title.ilike(f"%{search}%"),
            Job.company.ilike(f"%{search}%"),
            Job.location.ilike(f"%{search}%"),
            Job.description.ilike(f"%{search}%")
        )
    ).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/company/<company>", methods=["GET"])
def jobs_by_company(company):
    jobs = Job.query.filter_by(company=company).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/location/<location>", methods=["GET"])
def jobs_by_location(location):
    jobs = Job.query.filter_by(location=location).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/salary/<int:salary>", methods=["GET"])
def jobs_by_salary(salary):
    jobs = Job.query.filter(Job.salary >= salary).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/page", methods=["GET"])
def paginate_jobs():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    pagination = Job.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    jobs = [job.to_dict() for job in pagination.items]

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total_jobs": pagination.total,
        "total_pages": pagination.pages,
        "jobs": jobs
    }), 200

@jobs_bp.route("/my-jobs", methods=["GET"])
@jwt_required()
def my_jobs():

    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can view their jobs"
        }), 403

    recruiter_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(created_by=recruiter_id).all()

    return jsonify({
        "count": len(jobs),
        "jobs": [job.to_dict() for job in jobs]
    }), 200


@jobs_bp.route("/jobs/filter", methods=["GET"])
def filter_jobs():

    company = request.args.get("company")
    location = request.args.get("location")

    query = Job.query

    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    jobs = query.all()

    return jsonify({
        "count": len(jobs),
       "jobs": [job.to_dict() for job in jobs]
    }), 200

@jobs_bp.route("/jobs/<int:job_id>/save", methods=["POST"])
@jwt_required()
def save_job(job_id):

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
            "message": "Only candidates can save jobs"
        }), 403

    candidate_id = int(get_jwt_identity())

    job = db.session.get(Job, job_id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404

    existing = SavedJob.query.filter_by(
        candidate_id=candidate_id,
        job_id=job_id
    ).first()

    if existing:
        return jsonify({
            "message": "Job already saved"
        }), 400

    saved = SavedJob(
        candidate_id=candidate_id,
        job_id=job_id
    )

    db.session.add(saved)
    db.session.commit()

    return jsonify({
        "message": "Job saved successfully"
    }), 201

@jobs_bp.route("/jobs/<int:job_id>/save", methods=["DELETE"])
@jwt_required()
def remove_saved_job(job_id):

    claims = get_jwt()

    if claims["role"] != "candidate":
        return jsonify({
            "message": "Only candidates can remove saved jobs"
        }), 403

    candidate_id = int(get_jwt_identity())

    saved_job = SavedJob.query.filter_by(
        candidate_id=candidate_id,
        job_id=job_id
    ).first()

    if not saved_job:
        return jsonify({
            "message": "Saved job not found"
        }), 404

    db.session.delete(saved_job)
    db.session.commit()

    return jsonify({
        "message": "Saved job removed successfully"
    }), 200

@jobs_bp.route("/jobs/<int:id>", methods=["GET"])
@jwt_required()
def get_single_job(id):

    job = db.session.get(Job, id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404


    claims = get_jwt()

    # Only candidates should get recent viewed history
    if claims["role"] == "candidate":

        candidate_id = int(get_jwt_identity())

        existing = RecentlyViewedJob.query.filter_by(
            candidate_id=candidate_id,
            job_id=id
        ).first()


        if not existing:

            viewed_job = RecentlyViewedJob(
                candidate_id=candidate_id,
                job_id=id
            )

            db.session.add(viewed_job)
            db.session.commit()


    return jsonify(job.to_dict()), 200