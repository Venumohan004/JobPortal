from datetime import datetime
from . import db


class RecentlyViewedJob(db.Model):

    __tablename__ = "recently_viewed_jobs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

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

    viewed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )