from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt


def candidate_required(fn):
    """Allow access only to users with the candidate role."""
    @wraps(fn)
    def wrapper(*args, **kwargs):

        claims = get_jwt()

        if claims.get("role") != "candidate":
            return jsonify({
                "message": "Access denied. Candidate role required."
            }), 403

        return fn(*args, **kwargs)

    return wrapper
