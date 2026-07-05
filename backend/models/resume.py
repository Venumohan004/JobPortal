from models import db

class Resume(db.Model):
    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "file_name": self.file_name,
            "file_path": self.file_path
        }