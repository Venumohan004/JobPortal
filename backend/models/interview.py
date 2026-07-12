from models import db

class Interview(db.Model):

    __tablename__="interviews"

    id=db.Column(db.Integer,primary_key=True)

    application_id=db.Column(
        db.Integer,
        db.ForeignKey("applications.id")
    )

    interview_date=db.Column(db.String(30))

    interview_time=db.Column(db.String(30))

    mode=db.Column(db.String(50))

    meeting_link=db.Column(db.String(500))