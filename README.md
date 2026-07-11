# Job Portal Backend

A production-ready **RESTful Job Portal Backend** built using **Python, Flask, MySQL, SQLAlchemy, JWT Authentication, and Flask-Mail**.

---

# 🚀 Tech Stack

- Python
- Flask
- MySQL
- SQLAlchemy ORM
- Flask-JWT-Extended
- Flask-Mail
- Flask-Migrate
- Flask-CORS
- JWT Authentication
- Postman
- Git & GitHub

---

# 📂 Project Structure

```text
backend/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── job.py
│   ├── application.py
│   └── saved_job.py
│
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── jobs.py
│   ├── application.py
│   ├── resume.py
│   ├── saved_jobs.py
│   └── admin.py
│
├── utils/
│   └── email_service.py
│
├── uploads/
│   ├── resumes/
│   └── profile_images/
│
├── migrations/
│
└── templates/
```

---

# ✨ Features Implemented

## ✅ Authentication Module

- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Protected Routes
- User Profile
- Forgot Password
- Reset Password via Email

---

## ✅ Role-Based Access Control (RBAC)

- Admin
- Recruiter
- Candidate

Each role has access only to authorized APIs.

---

## ✅ Candidate Module

- Create Candidate Profile
- View Candidate Profile
- Update Candidate Profile

---

## ✅ Recruiter Module

- Create Recruiter Profile
- View Recruiter Profile
- Update Recruiter Profile

---

## ✅ Job Management

- Create Job
- Update Job
- Delete Job
- View All Jobs
- Search Jobs
- Filter by Company
- Filter by Location
- Filter by Salary
- Pagination
- Recruiter View My Jobs

---

## ✅ Job Application Module

- Apply for Job
- Prevent Duplicate Applications
- View Applied Jobs
- Delete Application
- Recruiter View Applications
- Update Application Status

---

## ✅ Resume Management

- Upload Resume
- Download Resume
- View Resume
- Delete Resume
- Upload Profile Image

---

## ✅ Saved Jobs

- Save Job
- View Saved Jobs
- Remove Saved Job

---

## ✅ Candidate Dashboard

- Total Applications
- Saved Jobs Count
- Recent Applications

---

## ✅ Recruiter Dashboard

- Total Jobs Posted
- Total Applications Received
- Recent Jobs
- Recent Applications

---

## ✅ Admin Module

### User Management

- View All Users
- Delete User
- Prevent Admin Account Deletion

### Admin Dashboard

- Total Users
- Total Recruiters
- Total Candidates
- Total Jobs
- Total Applications
- Pending Applications
- Accepted Applications
- Rejected Applications
- Latest Registered Users
- Latest Jobs
- Latest Applications

---

## ✅ Email Integration

- Welcome Email
- Forgot Password Email
- Password Reset Email

---

# 🔒 Security Features

- Password Hashing
- JWT Authentication
- Role-Based Authorization
- Protected Routes
- Environment Variables (.env)
- Secure Gmail SMTP Configuration

---

# 🛠 Database

MySQL with SQLAlchemy ORM.

## Tables

- Users
- Candidates
- Recruiters
- Jobs
- Applications
- Saved Jobs

---

# 📬 API Testing

All APIs have been tested using **Postman**.

### Authentication APIs

- Register
- Login
- Profile
- Forgot Password
- Reset Password

### Candidate APIs

- Create Profile
- View Profile
- Update Profile

### Recruiter APIs

- Create Profile
- View Profile
- Update Profile

### Job APIs

- Create Job
- Update Job
- Delete Job
- Get Jobs
- Search Jobs
- Filter Jobs
- Pagination

### Application APIs

- Apply Job
- View Applications
- Delete Application
- Recruiter View Applications
- Update Status

### Resume APIs

- Upload Resume
- Download Resume
- Delete Resume
- Upload Profile Image

### Saved Job APIs

- Save Job
- View Saved Jobs
- Delete Saved Job

### Admin APIs

- View All Users
- Delete User
- Admin Dashboard

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

Go to project folder

```bash
cd JobPortal/backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure the `.env` file

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret

DB_HOST=localhost
DB_PORT=3306
DB_NAME=job_portal
DB_USER=root
DB_PASSWORD=your_password

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
```

Run the application

```bash
python app.py
```

Server

```
http://127.0.0.1:5000
```

---

# 📌 Project Progress

## ✅ Day 1
- Project Setup

## ✅ Day 2
- MySQL Configuration

## ✅ Day 3
- User Model

## ✅ Day 4
- Registration API

## ✅ Day 5
- Login API
- JWT Authentication

## ✅ Day 6
- Role-Based Access Control

## ✅ Day 7
- Job CRUD APIs

## ✅ Day 8
- Job Search APIs

## ✅ Day 9
- Job Application System

## ✅ Day 10
- Recruiter Application Management

## ✅ Day 11
- Admin User Management

## ✅ Day 12
- Flask-Mail Integration

## ✅ Day 13
- Forgot Password & Reset Password

## ✅ Day 14
- Candidate Profile Module

## ✅ Day 15
- Recruiter Profile Module

## ✅ Day 16
- Recruiter Dashboard

## ✅ Day 17
- Candidate Dashboard

## ✅ Day 18
- Admin Dashboard
- Admin Statistics
- Latest Users
- Latest Jobs
- Latest Applications
- Delete User with Related Data Handling

---

# 🚀 Upcoming Features

- Advanced Search Filters
- Sorting
- Pagination Improvements
- Bookmark Enhancements
- Notifications
- Swagger API Documentation
- Unit Testing
- Docker
- CI/CD
- Deployment (Render / Railway / AWS)

---

# 👨‍💻 Author

**P. Venumohan**

🎓 B.Tech – Computer Science & Data Science

💻 Python | Flask | MySQL | SQLAlchemy | REST API

🔗 GitHub: https://github.com/Venumohan004

---

## ⭐ If you found this project useful, don't forget to Star the repository!
