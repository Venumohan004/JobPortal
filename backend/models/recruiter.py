from models import db

class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    company_email = db.Column(db.String(120), unique=True, nullable=False)
    company_location = db.Column(db.String(100))
    company_website = db.Column(db.String(150))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    # Add this here
    user = db.relationship("User", backref="recruiter")

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "company_email": self.company_email,
            "company_location": self.company_location,
            "company_website": self.company_website,
            "user_id": self.user_id
        }