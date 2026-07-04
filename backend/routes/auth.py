from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db
from models.user import User
import bcrypt

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
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

    return jsonify({
        "message": "Registration Successful"
    }), 201


# -------------------------------
# Login API
# -------------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return jsonify({
            "message": "Login API is working. Please use POST with JSON data."
        })

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "message": "Please send JSON data with Content-Type: application/json"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and Password are required"
        }), 400

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
        "token": access_token,
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }
    }), 200

@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()
    claims = get_jwt()

    return jsonify({
        "message": "Protected Route Accessed Successfully",
        "user": {
            "id": user_id,
            "email": claims.get("email"),
            "role": claims.get("role")
        }
    }), 200