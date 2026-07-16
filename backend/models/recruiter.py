from models import db
from datetime import datetime

class Recruiter(db.Model):
    """Represents a recruiter profile."""
    __tablename__ = "recruiters"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    company_email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )
    company_location = db.Column(db.String(100))
    company_website = db.Column(db.String(150))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )
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
            "company_name": self.company_name,
            "company_email": self.company_email,
            "company_location": self.company_location,
            "company_website": self.company_website,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
    def __repr__(self):
        return f"<Recruiter {self.company_name}>"