from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from models import db

from routes.auth import auth
from routes.candidate import candidate

app = Flask(__name__)

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


@app.route("/")
def home():
    return {
        "message": "Job Portal Backend is Running",
        "status": "success"
    }


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    print(app.url_map)
    
    app.run(debug=True)