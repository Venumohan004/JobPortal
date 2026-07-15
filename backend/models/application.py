from models import db
from datetime import datetime

class Application(db.Model):
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
            "created_at": self.created_at.isoformat() if self.created_at else None
        }