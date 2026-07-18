from models import db
from datetime import datetime


class Interview(db.Model):
    __tablename__ = "interviews"

    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("applications.id"),
        nullable=False
    )

    interview_date = db.Column(db.String(30), nullable=False)

    interview_time = db.Column(db.String(30), nullable=False)

    mode = db.Column(db.String(50), nullable=False)

    meeting_link = db.Column(db.String(500))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    application = db.relationship(
        "Application",
        backref="interviews",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "application_id": self.application_id,
            "interview_date": self.interview_date,
            "interview_time": self.interview_time,
            "mode": self.mode,
            "meeting_link": self.meeting_link,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }