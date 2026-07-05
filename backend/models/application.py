from models import db

class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="Applied")

    def to_dict(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "job_id": self.job_id,
            "status": self.status
        }