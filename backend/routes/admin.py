from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.user import User

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/users", methods=["GET"])
@jwt_required()
def get_users():

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user or user.role != "admin":
        return jsonify({"message": "Access Denied"}), 403

    users = User.query.all()

    return jsonify({
        "count": len(users),
        "users": [
            {
                "id": u.id,
                "email": u.email,
                "role": u.role
            } for u in users
        ]
    }), 200