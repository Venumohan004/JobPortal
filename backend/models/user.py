from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15))

    role = db.Column(
        db.Enum("candidate", "recruiter", "admin"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)