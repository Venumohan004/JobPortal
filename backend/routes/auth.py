from flask import Blueprint, request, jsonify, current_app

import bcrypt

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from models import db
from models.user import User

from utils.email import send_email
from utils.token_helper import (
    generate_reset_token,
    verify_reset_token
)

auth = Blueprint("auth", __name__)


# -------------------------------
# Test Route
# -------------------------------
@auth.route("/test", methods=["GET"])
def test():
    return jsonify({
        "message": "Auth Route Working"
    })


# -------------------------------
# Register API
# -------------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():
    try:

        if request.method == "GET":
            return jsonify({
                "message": "Register API is working. Please use POST with JSON data."
            })

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "message": "Please send JSON data with Content-Type: application/json"
            }), 400

        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        role = data.get("role")

        if role not in ["candidate", "recruiter", "admin"]:
            return jsonify({
                "message": "Invalid role"
            }), 400

        if not all([full_name, email, password, role]):
            return jsonify({
                "message": "Required fields are missing"
            }), 400

        existing = User.query.filter_by(email=email).first()

        if existing:
            return jsonify({
                "message": "Email already exists"
            }), 400

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        user = User(
            full_name=full_name,
            email=email,
            password=hashed_password.decode("utf-8"),
            phone=phone,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        # send_email(
        #     subject="Welcome to Job Portal",
        #     recipients=[user.email],
        #     body=f"""
        #     Hello {user.full_name},

        #     Welcome to Job Portal!

        #     Your account has been created successfully.

        #     Happy Job Hunting!

        #     Regards,
        #     Job Portal Team
        #     """
        #     )

        return jsonify({
            "message": "Registration Successful"
        }), 201

    except Exception as e:
        print("REGISTER ERROR:", e)
        return jsonify({"error": str(e)}), 500

# -------------------------------
# Login API
# -------------------------------
@auth.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "message": "Please send JSON data"
            }), 400

        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({
                "message": "Invalid Email"
            }), 401

        if not bcrypt.checkpw(
            password.encode("utf-8"),
            user.password.encode("utf-8")
        ):
            return jsonify({
                "message": "Invalid Password"
            }), 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "email": user.email,
                "role": user.role
            }
        )

        return jsonify({
            "message": "Login Successful",
            "token": access_token
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "error": str(e)
        }), 500
    
@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = db.session.get(User, int(user_id))

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    return jsonify({
        "message": "Protected Route Accessed Successfully",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }
    }), 200

@auth.route("/forgot-password", methods=["POST"])
def forgot_password():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
        "message": "Please send JSON data"
    }), 400

    email = data.get("email")

    if not email:
        return jsonify({
            "message": "Email is required"
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Email not found"
        }), 404

    token = generate_reset_token(user.email)

    reset_link = (
        f"{current_app.config['FRONTEND_URL']}/reset-password/{token}"
    )

    send_email(
        subject="Password Reset",
        recipients=[user.email],
        body=f"""
Hello {user.full_name},

Click the link below to reset your password.

{reset_link}

This link will expire in 30 minutes.

Regards,
Job Portal Team
"""
    )

    return jsonify({
        "message": "Password reset link sent successfully"
    }), 200

@auth.route("/reset-password/<token>", methods=["POST"])
def reset_password(token):

    data = request.get_json()

    new_password = data.get("password")

    if not new_password:
        return jsonify({
            "message": "Password is required"
        }), 400

    email = verify_reset_token(token)

    if not email:
        return jsonify({
            "message": "Invalid or expired token"
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    hashed_password = bcrypt.hashpw(
        new_password.encode("utf-8"),
        bcrypt.gensalt()
    )

    user.password = hashed_password.decode("utf-8")

    db.session.commit()

    return jsonify({
        "message": "Password reset successfully"
    }), 200