from models import db
from datetime import datetime

class Application(db.Model):
    """Represents a candidate's application for a job."""
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
    )
    job_id = db.Column(
    db.Integer,
    db.ForeignKey("jobs.id"),
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
    default="Applied",
    nullable=False
    )

    created_at = db.Column(
    db.DateTime,
    default=datetime.utcnow,
    nullable=False
    )
    candidate = db.relationship(
        "User",
        back_populates="applications"
    )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    __table_args__ = (
    db.UniqueConstraint(
        "candidate_id",
        "job_id",
        name="uq_candidate_job"
    ),
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "job_id": self.job_id,
            "status": self.status,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    def __repr__(self):
        return (
            f"<Application {self.id}: "
            f"Candidate {self.candidate_id} -> Job {self.job_id}>"
        )