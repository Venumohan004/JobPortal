from datetime import datetime
from models import db


class ApplicationStatusHistory(db.Model):
    __tablename__ = "application_status_history"

    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("applications.id"),
        nullable=False
    )

    old_status = db.Column(db.String(50), nullable=False)
    new_status = db.Column(db.String(50), nullable=False)

    changed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    application = db.relationship(
        "Application",
        backref="status_history"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "application_id": self.application_id,
            "old_status": self.old_status,
            "new_status": self.new_status,
            "changed_at": self.changed_at.isoformat()
        }