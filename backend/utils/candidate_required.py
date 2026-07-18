from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify

from models import User


def candidate_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):

        current_user = int(get_jwt_identity())

        user = User.query.get(current_user)

        print("JWT Identity:", current_user)
        print("User:", user)
        print("Role:", user.role if user else None)

        if not user:
            return jsonify({"message": "User not found"}), 404

        if user.role != "candidate":
            return jsonify({"message": "Candidate access required"}), 403

        return fn(*args, **kwargs)

    return wrapper