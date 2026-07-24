import os

# Allowed extensions
IMAGE_EXTENSIONS = {"png", "jpg", "jpeg"}
RESUME_EXTENSIONS = {"pdf", "doc", "docx"}


def allowed_file(filename, allowed_extensions):
    """
    Check whether the uploaded file has an allowed extension.
    """

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )


def get_file_extension(filename):
    """
    Return the lowercase file extension.
    """

    return os.path.splitext(filename)[1].lower()