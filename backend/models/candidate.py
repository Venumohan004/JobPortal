from . import db
from datetime import datetime

class Candidate(db.Model):
    """Represents a candidate profile."""
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    skills = db.Column(db.String(150))
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    address = db.Column(db.Text)
    about = db.Column(db.Text)
    location = db.Column(db.String(100))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "skills": self.skills,
            "education": self.education,
            "experience": self.experience,
            "address": self.address,
            "about": self.about,
            "location": self.location,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    def __repr__(self):
        return f"<Candidate {self.user_id}>"