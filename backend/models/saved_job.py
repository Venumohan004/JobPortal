from datetime import datetime
from models import db


class SavedJob(db.Model):
    __tablename__ = "saved_jobs"

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

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        db.UniqueConstraint(
            "candidate_id",
            "job_id",
            name="unique_saved_job"
        ),
    )

    candidate = db.relationship(
        "User",
        backref=db.backref(
            "saved_jobs",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )

    job = db.relationship(
        "Job",
        backref=db.backref(
            "saved_by",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )

    def to_dict(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "job_id": self.job_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }