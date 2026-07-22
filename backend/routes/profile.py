from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.user import User

profile_bp = Blueprint("profile", __name__)


# =====================================
# Get Logged-in User Profile
# =====================================

@profile_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():

    user = db.session.get(User, int(get_jwt_identity()))

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify({
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "location": user.location,
        "skills": user.skills,
        "bio": user.bio,
        "profile_image": user.profile_image,
        "role": user.role
    }), 200


# =====================================
# Update Logged-in User Profile
# =====================================

@profile_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    user = db.session.get(User, int(get_jwt_identity()))

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "JSON data required"
        }), 400

    user.full_name = data.get("full_name", user.full_name)
    user.phone = data.get("phone", user.phone)
    user.location = data.get("location", user.location)
    user.skills = data.get("skills", user.skills)
    user.bio = data.get("bio", user.bio)

    try:
        db.session.commit()

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "message": "Failed to update profile",
            "error": str(e)
        }), 500

    return jsonify({
        "message": "Profile updated successfully",
        "profile": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "location": user.location,
            "skills": user.skills,
            "bio": user.bio,
            "profile_image": user.profile_image
        }
    }), 200