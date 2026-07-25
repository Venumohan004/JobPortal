import os
from flasgger import Swagger
from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from models import db
from extensions import mail, migrate

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
from routes.profile import profile_bp
from routes.candidate_interview_routes import candidate_interview_bp

from flask import jsonify
from models import db

from flask_mail import Message
from extensions import mail

app = Flask(__name__)

Swagger(app)
# =====================
# Load Configuration
# =====================

app.config.from_object(Config)

# =====================
# Enable CORS
# =====================

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
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
migrate.init_app(app, db)

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
app.register_blueprint(profile_bp)
app.register_blueprint(candidate_interview_bp)




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
@app.route("/debug/db")
def debug_db():
    db_name = db.session.execute(
        db.text("SELECT current_database()")
    ).scalar()

    enum_values = db.session.execute(
        db.text("""
        SELECT enumlabel
        FROM pg_enum
        JOIN pg_type
        ON pg_enum.enumtypid = pg_type.oid
        WHERE typname='application_status'
        ORDER BY enumsortorder;
        """)
    ).fetchall()

    return jsonify({
        "database": db_name,
        "enum": [row[0] for row in enum_values]
    })

@app.route("/test-mail")
def test_mail():
    try:
        msg = Message(
            subject="Render Mail Test",
            recipients=["pvenumohan831@gmail.com"],
            body="This is a test email from Flask-Mail on Render."
        )

        mail.send(msg)

        return {
            "message": "Email sent successfully"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "error": str(e)
        }, 500

@app.route("/mail-debug")
def mail_debug():
    return {
        "MAIL_SERVER": app.config.get("MAIL_SERVER"),
        "MAIL_PORT": app.config.get("MAIL_PORT"),
        "MAIL_USE_TLS": app.config.get("MAIL_USE_TLS"),
        "MAIL_USE_SSL": app.config.get("MAIL_USE_SSL"),
        "MAIL_TIMEOUT": app.config.get("MAIL_TIMEOUT"),
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

#checking 
@app.route("/check-enum")
def check_enum():
    from models.application import Application
    return {
        "enum": Application.status.type.enums
    }



