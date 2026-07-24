from flask_jwt_extended import get_jwt_identity

from models.user import User


def get_current_user():
    """
    Return the currently authenticated user object.
    """

    user_id = get_jwt_identity()

    if not user_id:
        return None

    return User.query.get(int(user_id))


def is_admin():
    """
    Check if the current user is an admin.
    """

    user = get_current_user()

    return bool(user and user.role == "admin")


def is_recruiter():
    """
    Check if the current user is a recruiter.
    """

    user = get_current_user()

    return bool(user and user.role == "recruiter")


def is_candidate():
    """
    Check if the current user is a candidate.
    """

    user = get_current_user()

    return bool(user and user.role == "candidate")