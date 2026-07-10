from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .job import Job
from .application import Application
from .recruiter import Recruiter
from .candidate import Candidate