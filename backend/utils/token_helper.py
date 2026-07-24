from flask import current_app
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired


def generate_reset_token(email):
    """
    Generate a password reset token.
    """

    serializer = URLSafeTimedSerializer(
        current_app.config["SECRET_KEY"]
    )

    return serializer.dumps(
        email,
        salt="password-reset-salt"
    )


def verify_reset_token(token, expiration=1800):
    """
    Verify password reset token.

    Args:
        token (str): Reset token
        expiration (int): Expiration time in seconds (default 30 min)

    Returns:
        str | None: Email if valid, otherwise None
    """

    serializer = URLSafeTimedSerializer(
        current_app.config["SECRET_KEY"]
    )

    try:
        email = serializer.loads(
            token,
            salt="password-reset-salt",
            max_age=expiration
        )

        return email

    except (SignatureExpired, BadSignature):
        return None