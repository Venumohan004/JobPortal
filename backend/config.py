import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)


    # Render PostgreSQL Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Email Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")


    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    RESUME_FOLDER = os.path.join(UPLOAD_FOLDER, "resumes")
    PROFILE_FOLDER = os.path.join(UPLOAD_FOLDER, "profile_images")


    MAX_CONTENT_LENGTH = 16 * 1024 * 1024