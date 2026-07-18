from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .job import Job
from .application import Application
from .recruiter import Recruiter
from .candidate import Candidate
from .resume import Resume
from .saved_job import SavedJob
from .recently_viewed_job import RecentlyViewedJob
from .interview import Interview