from models import db

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
    status = db.Column(db.String(50), default="Applied")

    candidate = db.relationship("User", backref="applications")
    job = db.relationship("Job", backref="applications")
    
    def to_dict(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "job_id": self.job_id,
            "status": self.status
        }