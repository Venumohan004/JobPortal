from . import db
from datetime import datetime


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(db.String(15))


    role = db.Column(
        db.Enum(
            "candidate",
            "recruiter",
            "admin",
            name="user_role"
        ),
        default="candidate",
        nullable=False
    )


    status = db.Column(
        db.Enum(
            "Applied",
            "Shortlisted",
            "Rejected",
            "Selected",
            name="application_status"
        ),
        default="Applied"
    )


    resume = db.Column(db.String(255))

    profile_image = db.Column(db.String(255))

    location = db.Column(db.String(100))

    bio = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )