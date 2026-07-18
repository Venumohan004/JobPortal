import os
import traceback
from flask import Blueprint, request, jsonify, current_app, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename

from models import db
from models.resume import Resume
from models.user import User
from utils.file_helper import allowed_file, IMAGE_EXTENSIONS, RESUME_EXTENSIONS
from config import Config

resume_bp = Blueprint("resume", __name__)


# ==========================================================
# Upload Resume
# ==========================================================
@resume_bp.route("/upload/resume", methods=["POST"])
@jwt_required()
def upload_resume():
    try:
        if "resume" not in request.files:
            return jsonify({"message": "No file uploaded"}), 400

        file = request.files["resume"]

        if file.filename == "":
            return jsonify({"message": "No selected file"}), 400

        if not allowed_file(file.filename, RESUME_EXTENSIONS):
            return jsonify({
                "message": "Only PDF files are allowed"
            }), 400

        filename = secure_filename(file.filename)

        upload_folder = current_app.config["RESUME_FOLDER"]
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, filename)

        candidate_id = get_jwt_identity()

        # Check if resume already exists
        existing_resume = Resume.query.filter_by(
            candidate_id=candidate_id
        ).first()

        if existing_resume:

            # Delete old file
            if os.path.exists(existing_resume.file_path):
                os.remove(existing_resume.file_path)

            # Save new file
            file.save(filepath)

            existing_resume.file_name = filename
            existing_resume.file_path = filepath

            db.session.commit()

            return jsonify({
                "message": "Resume updated successfully",
                "resume": existing_resume.to_dict()
            }), 200

        # Save new file
        file.save(filepath)

        new_resume = Resume(
            candidate_id=candidate_id,
            file_name=filename,
            file_path=filepath
        )

        db.session.add(new_resume)
        db.session.commit()

        return jsonify({
            "message": "Resume uploaded successfully",
            "resume": new_resume.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

        return jsonify({
            "message": "Internal Server Error",
            "error": str(e)
        }), 500


# ==========================================================
# Get Resume
# ==========================================================
@resume_bp.route("/resume/<int:candidate_id>", methods=["GET"])
def get_resume(candidate_id):

    resume = Resume.query.filter_by(
        candidate_id=candidate_id
    ).first()

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    return jsonify(resume.to_dict()), 200


# ==========================================================
# Download Resume
# ==========================================================
@resume_bp.route("/resume/download/<int:candidate_id>", methods=["GET"])
def download_resume(candidate_id):

    resume = Resume.query.filter_by(
        candidate_id=candidate_id
    ).first()

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    return send_from_directory(
        current_app.config["RESUME_FOLDER"],
        resume.file_name,
        as_attachment=True
    )


# ==========================================================
# Delete Resume
# ==========================================================
@resume_bp.route("/resume/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_resume(id):

    resume = Resume.query.get(id)

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    if os.path.exists(resume.file_path):
        os.remove(resume.file_path)

    db.session.delete(resume)
    db.session.commit()

    return jsonify({
        "message": "Resume deleted successfully"
    }), 200


# ==========================================================
# Upload Profile Image
# ==========================================================
@resume_bp.route("/upload/profile-image", methods=["POST"])
@jwt_required()
def upload_profile_image():

    try:

        user_id = get_jwt_identity()

        if "image" not in request.files:
            return jsonify({
                "message": "No image uploaded"
            }), 400

        file = request.files["image"]

        if file.filename == "":
            return jsonify({
                "message": "No selected image"
            }), 400

        if not allowed_file(file.filename, IMAGE_EXTENSIONS):
            return jsonify({
                "message": "Only JPG, JPEG and PNG files are allowed"
            }), 400

        filename = secure_filename(file.filename)

        os.makedirs(Config.PROFILE_FOLDER, exist_ok=True)

        filepath = os.path.join(
            Config.PROFILE_FOLDER,
            filename
        )

        file.save(filepath)

        user = User.query.get(user_id)

        if not user:
            return jsonify({
                "message": "User not found"
            }), 404

        user.profile_image = filename

        db.session.commit()

        return jsonify({
            "message": "Profile image uploaded successfully",
            "filename": filename
        }), 200

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()

        return jsonify({
            "message": "Internal Server Error",
            "error": str(e)
        }), 500