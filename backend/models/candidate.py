from . import db


class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    skills = db.Column(db.String(150))
    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    address = db.Column(db.Text)
    about = db.Column(db.Text)
    location = db.Column(db.String(100))

    user = db.relationship("User", backref="candidate", lazy=True)