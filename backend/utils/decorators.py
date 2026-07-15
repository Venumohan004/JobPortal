from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt


def candidate_required(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        claims = get_jwt()

        if claims.get("role") != "candidate":
            return jsonify({
                "message": "Only candidates allowed"
            }), 403

        return fn(*args, **kwargs)

    return wrapper