import os

from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from config import Config
from models import db

# Routes
from routes.auth import auth
from routes.candidate import candidate
from routes.recruiter import recruiter_bp
from routes.jobs import jobs_bp
from routes.application import application_bp
from routes.resume import resume_bp
from routes.saved_jobs import saved_bp
from routes.admin import admin_bp
from routes.interview import interview_bp

# Email
from utils.email import mail, send_email

app = Flask(__name__)

# =====================
# Load Configuration
# =====================

app.config.from_object(Config)

# =====================
# Enable CORS (FIXED)
# =====================

CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "http://localhost:5173",
                "http://localhost:5174"
                # Add your deployed frontend URL later, e.g.
                # "https://your-frontend.vercel.app"
            ]
        }
    },
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

# =====================
# Create Upload Folders
# =====================

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["RESUME_FOLDER"], exist_ok=True)
os.makedirs(app.config["PROFILE_FOLDER"], exist_ok=True)

# =====================
# Initialize Extensions
# =====================

db.init_app(app)
jwt = JWTManager(app)
mail.init_app(app)
migrate = Migrate(app, db)

# =====================
# Register Blueprints
# =====================

app.register_blueprint(auth)
app.register_blueprint(candidate)
app.register_blueprint(recruiter_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(application_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(saved_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(interview_bp, url_prefix="/interviews")

# =====================
# Basic Routes
# =====================

@app.route("/")
def home():
    return {
        "message": "Job Portal Backend is Running",
        "status": "success"
    }

# =====================
# Frontend Pages
# =====================

@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/jobs-page")
def jobs_page():
    return render_template("jobs.html")


@app.route("/register-page")
def register_page():
    return render_template("register.html")


@app.route("/login-page")
def login_page():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/profile-page")
def profile_page():
    return render_template("profile.html")

# =====================
# Configuration Test
# =====================

@app.route("/config-test")
def config_test():
    return {
        "SECRET_KEY": bool(app.config.get("SECRET_KEY")),
        "JWT_SECRET_KEY": bool(app.config.get("JWT_SECRET_KEY")),
        "MAIL_SERVER": app.config.get("MAIL_SERVER"),
        "MAIL_PORT": app.config.get("MAIL_PORT"),
        "MAIL_USERNAME": app.config.get("MAIL_USERNAME"),
        "MAIL_DEFAULT_SENDER": app.config.get("MAIL_DEFAULT_SENDER"),
        "MAIL_USE_TLS": app.config.get("MAIL_USE_TLS")
    }

# =====================
# Error Handlers
# =====================

@app.errorhandler(404)
def not_found(_):
    return {"message": "Not Found"}, 404


@app.errorhandler(500)
def server_error(error):
    db.session.rollback()

    return {
        "message": "Internal Server Error",
        "error": str(error)
    }, 500

# =====================
# Run Application
# =====================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )