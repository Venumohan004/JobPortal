from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.candidate import Candidate

candidate = Blueprint("candidate", __name__)


# Create Candidate Profile
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

# Get Candidate Profile
@candidate.route("/candidate/profile", methods=["GET"])
@jwt_required()
def get_profile():

    user_id = int(get_jwt_identity())

    profile = Candidate.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    return jsonify({
        "id": profile.id,
        "skills": profile.skills,
        "education": profile.education,
        "experience": profile.experience,
        "address": profile.address,
        "about": profile.about,
        "location": profile.location
    })


# Update Candidate Profile
@candidate.route("/candidate/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    user_id = int(get_jwt_identity())

    profile = Candidate.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    data = request.get_json()

    profile.skills = data.get("skills", profile.skills)
    profile.education = data.get("education", profile.education)
    profile.experience = data.get("experience", profile.experience)
    profile.address = data.get("address", profile.address)
    profile.about = data.get("about", profile.about)
    profile.location = data.get("location", profile.location)

    db.session.commit()

    return jsonify({
        "message": "Candidate profile updated successfully"
    })