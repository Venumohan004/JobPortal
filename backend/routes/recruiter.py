from flask import Blueprint, request, jsonify
from models import db
from models.recruiter import Recruiter

recruiter_bp = Blueprint("recruiter", __name__)

@recruiter_bp.route("/recruiter", methods=["POST"])
def create_recruiter():

    data = request.get_json()

    recruiter = Recruiter(
        company_name=data["company_name"],
        company_email=data["company_email"],
        company_location=data["company_location"],
        company_website=data["company_website"],
        user_id=data["user_id"]
    )

    db.session.add(recruiter)
    db.session.commit()

    return jsonify({
        "message": "Recruiter Profile Created",
        "recruiter": recruiter.to_dict()
    }), 201