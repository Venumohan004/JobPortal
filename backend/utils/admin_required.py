from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify

from models import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):

        current_user = get_jwt_identity()

        user = User.query.get(current_user)

        if not user:
            return jsonify({"message":"User not found"}),404

        if user.role != "admin":
            return jsonify({"message":"Admin access required"}),403

        return fn(*args, **kwargs)

    return wrapper