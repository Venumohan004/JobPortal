from flask import Blueprint, request, jsonify
from models import db
from models.job import Job
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import get_jwt_identity
 

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

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    company = request.args.get("company")
    location = request.args.get("location")
    title = request.args.get("title", "")
    min_salary = request.args.get("min_salary", type=int)
    sort = request.args.get("sort")

    query = Job.query

    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    if title:
        query = query.filter(Job.title.ilike(f"%{title}%"))

    if min_salary:
        query = query.filter(Job.salary >= min_salary)

    if sort == "salary_asc":
        query = query.order_by(Job.salary.asc())
    elif sort == "salary_desc":
        query = query.order_by(Job.salary.desc())
    elif sort == "latest":
        query = query.order_by(Job.id.desc())
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

@jobs_bp.route("/jobs/<int:id>", methods=["PUT"])
@jwt_required()
def update_job(id):
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can update jobs"
        }), 403

    job = Job.query.get(id)

    if not job:
        return jsonify({
            "message": "Job not found"
        }), 404
    
    if job.created_by != int(get_jwt_identity()):
        return jsonify({
        "message": "You can update only your own jobs"
    }), 403

    data = request.get_json()

    job.title = data.get("title", job.title)
    job.company = data.get("company", job.company)
    job.location = data.get("location", job.location)
    job.salary = data.get("salary", job.salary)
    job.description = data.get("description", job.description)
     

    db.session.commit()

    return jsonify({
        "message": "Job Updated Successfully",
        "job": job.to_dict()
    }), 200

@jobs_bp.route("/jobs/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_job(id):
    claims = get_jwt()

    if claims["role"] != "recruiter":
        return jsonify({
            "message": "Only recruiters can delete jobs"
        }), 403

    job = Job.query.get(id)

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
    title = request.args.get("title", "")

    jobs = Job.query.filter(
        Job.title.ilike(f"%{title}%")
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