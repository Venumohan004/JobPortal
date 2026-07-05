from flask import Blueprint, request, jsonify
from models import db
from models.resume import Resume

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/resume", methods=["POST"])
def upload_resume():
    data = request.get_json()

    resume = Resume(
        candidate_id=data["candidate_id"],
        file_name=data["file_name"],
        file_path=data["file_path"]
    )

    db.session.add(resume)
    db.session.commit()

    return jsonify({
        "message": "Resume Uploaded Successfully",
        "resume": resume.to_dict()
    }), 201

@resume_bp.route("/resume/<int:candidate_id>", methods=["GET"])
def get_resume(candidate_id):
    resume = Resume.query.filter_by(candidate_id=candidate_id).first()

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    return jsonify(resume.to_dict()), 200

@resume_bp.route("/resume/<int:id>", methods=["PUT"])
def update_resume(id):
    resume = Resume.query.get(id)

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    data = request.get_json()

    resume.file_name = data["file_name"]
    resume.file_path = data["file_path"]

    db.session.commit()

    return jsonify({
        "message": "Resume Updated Successfully",
        "resume": resume.to_dict()
    }), 200

@resume_bp.route("/resume/<int:id>", methods=["DELETE"])
def delete_resume(id):
    resume = Resume.query.get(id)

    if not resume:
        return jsonify({
            "message": "Resume not found"
        }), 404

    db.session.delete(resume)
    db.session.commit()

    return jsonify({
        "message": "Resume Deleted Successfully"
    }), 200