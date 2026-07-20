import os

IMAGE_EXTENSIONS = {"png", "jpg", "jpeg"}
RESUME_EXTENSIONS = {"pdf", "doc", "docx"}

def allowed_file(filename, allowed_extensions):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )