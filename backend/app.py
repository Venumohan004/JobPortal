from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate

from config import Config
from models import db

from routes.auth import auth
from routes.candidate import candidate
from routes.recruiter import recruiter_bp
from routes.jobs import jobs_bp
from routes.application import application_bp
from routes.resume import resume_bp
from routes.saved_jobs import saved_bp

app = Flask(__name__)
migrate = Migrate(app, db)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(candidate)
app.register_blueprint(recruiter_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(application_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(saved_bp)

@app.route("/")
def home():
    return {
        "message": "Job Portal Backend is Running",
        "status": "success"
    }

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)