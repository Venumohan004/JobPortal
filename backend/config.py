import os
from datetime import timedelta
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()


class Config:

    # =========================
    # Security
    # =========================

    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)


    # =========================
    # Database Configuration
    # =========================

    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:
        # Render PostgreSQL
        if DATABASE_URL.startswith("postgres://"):
            DATABASE_URL = DATABASE_URL.replace(
                "postgres://",
                "postgresql://",
                1
            )

        SQLALCHEMY_DATABASE_URI = DATABASE_URL

    else:
        # Local MySQL
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))

        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True
    }


    # =========================
    # Mail Configuration
    # =========================
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))

    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    MAIL_TIMEOUT = 10
    
    # Frontend URL
    FRONTEND_URL = os.getenv(
            "FRONTEND_URL",
            "http://localhost:5173"
    )

    # =========================
    # Upload Folders
    # =========================

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    RESUME_FOLDER = os.path.join(UPLOAD_FOLDER, "resumes")

    PROFILE_FOLDER = os.path.join(UPLOAD_FOLDER, "profile_images")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024