from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from models import User


def recruiter_required(fn):
    """
    Allow access only to users with recruiter role.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):

        current_user_id = int(get_jwt_identity())

        user = User.query.get(current_user_id)

        if not user:
            return jsonify({"message": "User not found"}), 404

        if user.role != "recruiter":
            return jsonify({"message": "Recruiter access required"}), 403

        return fn(*args, **kwargs)

    return wrapper