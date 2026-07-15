from models import db
from datetime import datetime

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer)
    description = db.Column(db.Text)

    skills = db.Column(db.String(255))
    experience = db.Column(db.String(100))

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    created_at = db.Column(
    db.DateTime,
    default=datetime.utcnow,
    nullable=False
    )
    applications = db.relationship(
    "Application",
    backref="job",
    lazy=True,
    cascade="all, delete-orphan"
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "description": self.description,
            "skills": self.skills,
            "experience": self.experience,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }