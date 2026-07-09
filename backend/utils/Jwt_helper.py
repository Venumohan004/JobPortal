from flask_jwt_extended import get_jwt_identity
from models.user import User

def get_current_user():
    user_id = get_jwt_identity()
    return User.query.get(user_id)

def admin_required():
    user = get_current_user()

    if not user or user.role != "admin":
        return False

    return True

ALLOWED_RESUME_EXTENSIONS = {"pdf"}
ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename, allowed_extensions):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )