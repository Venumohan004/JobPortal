from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from models import db

from routes.auth import auth
from routes.candidate import candidate
from routes.recruiter import recruiter_bp

from routes.jobs import jobs_bp

from models.application import Application

from routes.application import application_bp

app = Flask(__name__)

# Load Configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize Database
db.init_app(app)

# Initialize JWT
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(candidate)
app.register_blueprint(recruiter_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(application_bp)

# Create Database Tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {
        "message": "Job Portal Backend is Running",
        "status": "success"
    }


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
