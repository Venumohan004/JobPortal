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
        nullable=False,
        index=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(db.String(20))


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

    candidate = db.relationship(
        "Candidate",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    recruiter = db.relationship(
        "Recruiter",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    jobs = db.relationship(
        "Job",
        backref="creator",
        lazy=True
    )

    applications = db.relationship(
        "Application",
        backref="candidate",
        lazy=True
    )

    resume = db.Column(db.String(255))

    profile_image = db.Column(db.String(255))

    location = db.Column(db.String(100))

    bio = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<User {self.email}>"