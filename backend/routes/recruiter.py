from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.recruiter import Recruiter
from models.user import User

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
