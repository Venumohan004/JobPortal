# 🚀 JobPortal – RESTful Backend API


<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)
![JWT](https://img.shields.io/badge/JWT-Authentication-green?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render)
![GitHub](https://img.shields.io/badge/Open%20Source-GitHub-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 💼 JobPortal Backend API

## 📊 Project Highlights

- RESTful API Architecture
- JWT Authentication
- Role-Based Authorization
- PostgreSQL Database
- Resume Management
- Interview Scheduling
- Flask-Mail Integration
- Alembic Migrations
- Render Deployment

## 🚀 Project Features

- 🔐 JWT Authentication & Authorization
- 👤 Candidate & Recruiter Management
- 💼 Job Posting & Job Search
- 📄 Resume Upload & Download
- ❤️ Saved Jobs
- 👀 Recently Viewed Jobs
- 📋 Job Applications
- 🎯 Interview Scheduling
- 📊 Admin Dashboard
- 📧 Email Notifications
- 🔍 Search, Filtering & Pagination
- ☁️ Render Deployment
- 🐘 PostgreSQL Database

A **production-ready RESTful Job Portal Backend API** developed using:

- Python
- Flask
- PostgreSQL
- SQLAlchemy ORM
- Flask-JWT-Extended
- Flask-Mail
- Flask-Migrate

This project provides complete backend functionality for an online recruitment platform.

### 👨‍🎓 Candidates can:

- Create profiles
- Upload resumes
- Search jobs
- Apply for jobs
- Save jobs
- Track applications

### 🏢 Recruiters can:

- Create company profiles
- Post jobs
- Manage applications
- Track hiring process

### 👑 Administrators can:

- Manage users
- Monitor jobs
- View applications
- Analyze platform activity


The project follows a modular architecture using:

- Flask Blueprints
- REST API Principles
- SQLAlchemy ORM
- JWT Security
- Role-Based Authorization

---

# 📌 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Design](#database-design)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Database Migration](#database-migration)
- [Running Application](#running-application)
- [Deployment](#deployment)
- [Interview Management](#interview-management)
- [API Modules](#api-modules)
- [API Endpoints](#api-endpoints)
- [Security](#security)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Developer](#developer)
- [License](#license)

---

# ✨ Features

## 🔐 Authentication

- User Registration
- Secure Login
- JWT Authentication
- Role-Based Authorization
- Password Hashing
- Forgot Password
- Password Reset Email
- Protected Routes


---

# 👨‍🎓 Candidate Features

- Candidate Profile Management
- Update Profile
- Resume Upload
- Resume Download
- Resume Delete
- Search Jobs
- Apply Jobs
- View Applied Jobs
- Save Jobs
- Remove Saved Jobs
- Recently Viewed Jobs
- Application Status Tracking
- Candidate Dashboard


---

# 🏢 Recruiter Features

- Recruiter Profile
- Company Profile
- Create Jobs
- Update Jobs
- Delete Jobs
- View Posted Jobs
- View Applications
- Accept Candidates
- Reject Candidates
- Shortlist Candidates
- Schedule Interviews
- Update Interviews
- Delete Interviews
- View Interviews
- Recruiter Dashboard
- Hiring Analytics
  
---

# 👑 Admin Features

- Admin Dashboard
- View Users
- View Candidates
- View Recruiters
- View Jobs
- View Applications
- Delete Users
- Delete Jobs
- Reports
- Platform Analytics


---

# 💼 Job Features

- Job CRUD Operations
- Advanced Job Search
- Company Search
- Location Search
- Salary Filtering
- Experience Filtering
- Skills Filtering
- Sorting
- Pagination


---

# 📄 Resume Management

- Upload Resume
- Download Resume
- Delete Resume
- PDF Validation
- Secure File Storage

---

# 🎯 Interview Management

- Schedule Interview
- View All Interviews
- View Interview Details
- Update Interview
- Delete Interview
- Google Meet / Zoom Meeting Support
- Recruiter Authorization
- Interview Tracking
- Recruiter-only Interview Scheduling
- JWT Protected Interview APIs
- Recruiter can schedule interviews only for job applicants
- Candidates can view interview details
---

# ❤️ Saved Jobs

- Save Job
- View Saved Jobs
- Remove Saved Jobs


---

# 👀 Recently Viewed Jobs

- Track Job Views
- View Recently Viewed Jobs


---

# 🏗️ Architecture

```
              Client
       (Postman / Frontend)

                |

                |

          Flask REST API

                |

 --------------------------------

 |              |               |

Routes       Services        Models

                |

             Database

              PostgreSQL

```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | Flask |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | Flask-JWT-Extended |
| Email Service | Flask-Mail |
| Migration | Flask-Migrate + Alembic |
| API Testing | Postman |
| Version Control | Git & GitHub |
| CORS | Flask-CORS |


---

# 📂 Project Structure


```
backend/

│
├── models/
│   ├── user.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── job.py
│   ├── application.py
│   ├── interview.py
│   ├── resume.py
│   ├── saved_job.py
│   └── recently_viewed_job.py
│
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── jobs.py
│   ├── application.py
│   ├── interview.py
│   ├── resume.py
│   └── admin.py
│
├── services/
│
├── utils/
│
├── migrations/
│
├── uploads/
│
├── instance/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md

```

---

# 🗄️ Database Design


```
                 User
                  |
        -------------------
        |                 |
   Candidate          Recruiter
        |                 |
        |                 |
     Application ---- Job
          |
          |
      Interview


     SavedJob
          |
          |
 RecentlyViewedJob

```

# ⚙️ Installation

## 1. Clone Repository


```bash
git clone https://github.com/Venumohan004/JobPortal.git

cd jobPortal
```


---

## 2. Create Virtual Environment


```bash
python -m venv venv
```


### Activate Environment


Windows:

```bash
venv\Scripts\activate
```


Linux / macOS:

```bash
source venv/bin/activate
```


---

## 3. Install Dependencies


```bash
pip install -r requirements.txt
```


---

# 🔑 Environment Configuration


Create `.env` file:


```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret_key


DATABASE_URL=postgresql://username:password@host/database

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

MAIL_USE_TLS=True
MAIL_USE_SSL=False

```


---

# 🗄️ Database Migration


Initialize migration:


```bash
flask db init
```


Create migration:


```bash
flask db migrate
```


Apply migration:


```bash
flask db upgrade
```


---

# ▶️ Running Application

Start Flask server:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

---

# ☁️ Deployment

The backend is deployed on Render.

**Production URL**

```text
https://jobportal-aver.onrender.com
```

---

## 🌐 Live API

**Base URL**

```text
https://jobportal-aver.onrender.com
```

---

# 📌 API Modules


| Module | Description |
|----------|------------------------------|
| Authentication | Register, Login, Password Reset |
| Candidate | Profile, Resume, Applications |
| Recruiter | Company Profile, Jobs, Analytics |
| Jobs | CRUD, Search, Filter, Pagination |
| Applications | Apply Jobs, Status Management |
| Resume | Upload, Download, Delete |
| Interview | Schedule, View, Update, Delete |
| Saved Jobs | Save & Remove Jobs |
| Admin | Dashboard & Reports |


---

# 🔗 API Endpoints


| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register User |
| POST | `/login` | Login User |
| GET | `/profile` | User Profile |
| GET | `/jobs` | Get All Jobs |
| POST | `/jobs` | Create Job |
| PUT | `/jobs/<id>` | Update Job |
| DELETE | `/jobs/<id>` | Delete Job |
| POST | `/jobs/<job_id>/apply` | Apply for a Job |
| GET | `/applications` | View Applications |
| POST | `/upload/resume` | Upload Resume |
| GET | `/admin/dashboard` | Admin Dashboard |
| POST | `/interviews` | Schedule Interview |
| GET | `/interviews` | Get All Interviews |
| GET | `/interviews/<id>` | Get Interview Details |
| PUT | `/interviews/<id>` | Update Interview |
| DELETE | `/interviews/<id>` | Delete Interview |


---

# 🔒 Security


Implemented security features:

✅ JWT Authentication  
✅ Password Hashing  
✅ Role-Based Authorization  
✅ Protected Routes  
✅ Input Validation  
✅ Secure Password Reset Tokens  
✅ File Upload Validation  


---

# 🧪 Testing


API testing performed using:

- Postman API Testing
- JWT Authentication Testing
- CRUD Testing
- Recruiter Workflow Testing
- Candidate Workflow Testing
- Interview Module Testing
- Database Migration Testing
- Render Deployment Testing


Example Login Response:

```json
{
    "message": "Login Successful",
    "token": "JWT_TOKEN"
}
```

---

# 🚀 Future Enhancements


- AI Resume Screening
- AI Candidate Ranking
- Interview Scheduling
- Interview Feedback System
- Calendar Integration
- Interview Reminder Emails
- Docker Deployment
- Swagger Documentation
- Unit Testing
- CI/CD Pipeline
- Redis Cache
- Elasticsearch Search
- Real-Time Notifications


---

# 👨‍💻 Developer


**P. Venumohan**

🎓 B.Tech - Computer Science & Data Science

💻 Python Backend Developer

📍 Andhra Pradesh, India


GitHub:

https://github.com/Venumohan004


---

# ⭐ Support


If you like this project, please consider giving it a ⭐ Star on GitHub.


---

# 📄 License


This project is licensed under the MIT License.


---

<p align="center">

Made with ❤️ using Python, Flask & PostgreSQL

</p>
