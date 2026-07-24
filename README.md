# 🚀 JobPortal – Full Stack Job Recruitment Platform (Flask + React + PostgreSQL)

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![Vite](https://img.shields.io/badge/Vite-Build%20Tool-646CFF?style=for-the-badge&logo=vite)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-green?style=for-the-badge)
![Flask-Mail](https://img.shields.io/badge/Flask-Mail-orange?style=for-the-badge)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 💼 JobPortal

## 📌 Project Overview

**JobPortal** is a production-ready **Full Stack Job Recruitment Platform** designed to connect **Candidates**, **Recruiters**, and **Administrators** through a secure and scalable web application.

The project consists of a **Flask REST API Backend**, a **React + Vite Frontend**, and a **PostgreSQL Database**, providing complete recruitment workflow management—from user authentication and job posting to interview scheduling and application tracking.

The application follows modern backend development practices including **RESTful API architecture**, **JWT Authentication**, **Role-Based Authorization**, **SQLAlchemy ORM**, **Alembic Database Migrations**, and **Email Notifications**.

---

## 🌐 Live Demo

### Frontend

https://jobportal-frontend-uojm.onrender.com

### Backend API

https://jobportal-aver.onrender.com

### GitHub Repository

https://github.com/Venumohan004/JobPortal

---

# 🌟 Project Highlights

- 🔐 Secure JWT Authentication
- 👥 Role-Based Authorization
- 💼 Complete Job Management
- 📄 Resume Upload & Download
- ❤️ Saved Jobs
- 👀 Recently Viewed Jobs
- 📋 Job Application Tracking
- 📊 Application Status History
- 📅 Interview Scheduling
- 📧 Email Notifications
- 📈 Recruiter Dashboard
- 👨‍💼 Candidate Dashboard
- 👑 Admin Dashboard
- 🔍 Search, Filtering & Pagination
- 🐘 PostgreSQL Database
- 🔄 Alembic Database Migrations
- 🌐 RESTful API Architecture
- ☁️ Render Deployment
- ⚛️ React Frontend

---

# 🚀 Key Features

## 🔐 Authentication & Security

- User Registration
- Secure Login
- JWT Authentication
- Role-Based Authorization
- Password Hashing
- Forgot Password
- Password Reset via Email
- Protected API Routes
- Secure File Upload Validation

---

## 👨‍🎓 Candidate Features

- Candidate Profile Management
- Update Personal Profile
- Resume Upload
- Resume Download
- Resume Delete
- Browse Available Jobs
- Search Jobs
- Filter Jobs
- Apply for Jobs
- View Applied Jobs
- Track Application Status
- View Application Status History
- Save Jobs
- Remove Saved Jobs
- Recently Viewed Jobs
- Candidate Dashboard
- View Scheduled Interviews

---

## 🏢 Recruiter Features

- Recruiter Profile Management
- Create Job Posts
- Edit Job Posts
- Delete Job Posts
- View Posted Jobs
- View Applicants
- Shortlist Candidates
- Reject Candidates
- Select Candidates
- Update Application Status
- View Application Status History
- Schedule Interviews
- View Scheduled Interviews
- Recruiter Dashboard
- Hiring Analytics
- Send Interview Notifications

---

## 👑 Admin Features

- Admin Dashboard
- Platform Analytics
- User Management
- Candidate Management
- Recruiter Management
- Job Management
- Application Monitoring
- Platform Statistics

---

## 💼 Job Management

- Create Jobs
- Update Jobs
- Delete Jobs
- Browse Jobs
- Search Jobs
- Company Search
- Location Search
- Salary Filtering
- Pagination
- Sorting
- Advanced Search

---

## 📄 Resume Management

- Upload Resume
- Download Resume
- Delete Resume
- PDF Validation
- Secure Storage

---

## 📋 Application Management

- Apply for Jobs
- Track Applications
- Application Status Updates
- Application Status History
- Recruiter Review Process
- Candidate Application Dashboard

---

## 🎯 Interview Management

- Schedule Interviews
- Update Interviews
- Delete Interviews
- View Interview Details
- Candidate Interview Dashboard
- Recruiter Interview Dashboard
- Google Meet Support
- Zoom Support
- Email Notifications
- JWT Protected APIs

---

## 📧 Email Notifications

The system automatically sends emails for:

- New Job Applications
- Application Status Updates
- Interview Scheduling
- Password Reset Requests

---

# 🏗️ System Architecture

```
                    React + Vite Frontend
                             │
                             │
                        Axios API Calls
                             │
                             ▼
                    Flask REST API Backend
                             │
      ┌──────────────┬──────────────┬──────────────┐
      │              │              │
 Authentication    Business      Email Service
   (JWT)            Logic        (Flask-Mail)
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
              SQLAlchemy ORM
                     │
                     ▼
             PostgreSQL Database
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | Flask |
| Frontend | React + Vite |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | Flask-JWT-Extended |
| Database Migration | Flask-Migrate + Alembic |
| Email Service | Flask-Mail |
| File Upload | Flask File Handling |
| API Testing | Postman |
| Frontend HTTP Client | Axios |
| Version Control | Git & GitHub |
| Deployment | Render |
| CORS | Flask-CORS |

---

# 📈 Project Workflow

```
Candidate
    │
    ▼
Register/Login
    │
    ▼
Browse Jobs
    │
    ▼
Apply for Job
    │
    ▼
Recruiter Reviews Application
    │
    ▼
Update Status
    │
    ▼
Interview Scheduled
    │
    ▼
Candidate Receives Email
    │
    ▼
Interview Process
```

---

# 📌 Table of Contents

- Project Overview
- Project Highlights
- Features
- System Architecture
- Tech Stack
- Project Structure
- Database Design
- Installation
- Environment Variables
- Database Migration
- Running the Application
- API Modules
- API Endpoints
- Security
- Testing
- Deployment
- Screenshots
- Future Enhancements
- Developer
- License
---

# 📂 Project Structure

```text
JobPortal/
│
├── backend/
│   │
│   ├── migrations/
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── application.py
│   │   ├── application_status_history.py
│   │   ├── candidate.py
│   │   ├── interview.py
│   │   ├── job.py
│   │   ├── recruiter.py
│   │   ├── resume.py
│   │   ├── saved_job.py
│   │   ├── recently_viewed_job.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── admin.py
│   │   ├── application.py
│   │   ├── auth.py
│   │   ├── candidate.py
│   │   ├── candidate_interview_routes.py
│   │   ├── interview.py
│   │   ├── jobs.py
│   │   ├── recruiter.py
│   │   └── resume.py
│   │
│   ├── utils/
│   │   ├── admin_required.py
│   │   ├── candidate_required.py
│   │   ├── recruiter_required.py
│   │   ├── email_utils.py
│   │   ├── file_helper.py
│   │   ├── Jwt_helper.py
│   │   └── token_helper.py
│   │
│   ├── uploads/
│   ├── templates/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── .gitignore
└── README.md
```

---

# 🗄️ Database Design

```text
                           USERS
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
     CANDIDATES                          RECRUITERS
          │                                     │
          │                                     │
          └──────────────┬──────────────────────┘
                         │
                        JOBS
                         │
                  APPLICATIONS
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
   INTERVIEWS     STATUS HISTORY      SAVED JOBS
                         │
                 RECENTLY VIEWED JOBS
```

---

# ⚙️ Installation Guide

Follow the steps below to set up the project locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

Move into the project directory.

```bash
cd JobPortal
```

---

## 2️⃣ Backend Setup

Navigate to the backend folder.

```bash
cd backend
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it.

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Frontend Setup

Open a new terminal.

```bash
cd frontend
```

Install Node.js dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

Frontend will be available at:

```text
http://localhost:5173
```

---

# 🔑 Environment Variables

Create a `.env` file inside the **backend** folder.

Example:

```env
# Flask

SECRET_KEY=your_secret_key

# JWT

JWT_SECRET_KEY=your_jwt_secret_key

# PostgreSQL

DATABASE_URL=postgresql://username:password@localhost/job_portal

# Email Configuration

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_USE_TLS=True
MAIL_USE_SSL=False

# Upload Folder

UPLOAD_FOLDER=uploads

# Application

FLASK_ENV=development
```

---

# 🐘 PostgreSQL Database Setup

Create a PostgreSQL database.

```sql
CREATE DATABASE job_portal;
```

Connect to the database.

```sql
\c job_portal
```

Grant privileges if required.

```sql
GRANT ALL PRIVILEGES
ON DATABASE job_portal
TO your_username;
```

---

# 🔄 Database Migration

Initialize Alembic (only once).

```bash
flask db init
```

Generate a migration.

```bash
flask db migrate -m "Initial migration"
```

Apply the migration.

```bash
flask db upgrade
```

Verify tables.

```sql
\dt
```

---

# ▶️ Running the Backend

Start the Flask development server.

```bash
python app.py
```

Backend will run at:

```text
http://127.0.0.1:5000
```

---

# 🌐 Running the Full Application

| Service | URL |
|----------|-----|
| Frontend | http://localhost:5173 |
| Backend | http://127.0.0.1:5000 |

---

# 📦 Backend Dependencies

Main Python packages used in this project:

- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Mail
- Flask-CORS
- SQLAlchemy
- psycopg2
- python-dotenv
- Werkzeug
- Gunicorn

---

# 📦 Frontend Dependencies

Main frontend technologies:

- React
- Vite
- React Router DOM
- Axios
- CSS3
- HTML5

---

# 💡 Development Tips

Before starting development, ensure that:

- ✅ PostgreSQL server is running.
- ✅ The `.env` file is configured correctly.
- ✅ Virtual environment is activated.
- ✅ Backend dependencies are installed.
- ✅ Frontend dependencies are installed.
- ✅ Database migrations have been applied.
- ✅ Both backend and frontend servers are running.

Once completed, you can access the full JobPortal application locally for development and testing.
---

# 📌 API Modules

The application is organized into modular Flask Blueprints for better maintainability and scalability.

| Module | Description |
|----------|-------------|
| Authentication | User registration, login, JWT authentication, forgot/reset password |
| Candidate | Candidate profile, dashboard, resume management |
| Recruiter | Recruiter profile, dashboard, company management |
| Jobs | Create, update, delete, search, filter, pagination |
| Applications | Apply for jobs, view applications, update application status |
| Interview | Schedule, update, delete and view interviews |
| Candidate Interviews | Candidate interview dashboard and interview details |
| Resume | Upload, download and delete resumes |
| Saved Jobs | Save, view and remove bookmarked jobs |
| Recently Viewed Jobs | Track recently viewed jobs |
| Admin | Dashboard, users, jobs and applications analytics |

---

# 🔗 API Endpoints

## 🔐 Authentication

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |
| GET | `/profile` | Get logged-in user profile |
| PUT | `/profile` | Update profile |
| POST | `/forgot-password` | Send password reset email |
| POST | `/reset-password` | Reset account password |

---

## 👨‍🎓 Candidate APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/candidate/profile` | Candidate profile |
| PUT | `/candidate/profile` | Update candidate profile |
| GET | `/my-applications` | View applied jobs |
| GET | `/my-interviews` | View scheduled interviews |
| GET | `/candidate/interviews/<id>` | Interview details |

---

## 💼 Job APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/jobs` | List all jobs |
| GET | `/jobs/<id>` | Job details |
| POST | `/jobs` | Create job |
| PUT | `/jobs/<id>` | Update job |
| DELETE | `/jobs/<id>` | Delete job |
| GET | `/jobs/search` | Search jobs |
| GET | `/jobs/company/<company>` | Search by company |
| GET | `/jobs/location/<location>` | Search by location |

---

## 📄 Application APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/jobs/<job_id>/apply` | Apply for a job |
| GET | `/applications` | View all applications (Recruiter/Admin) |
| GET | `/jobs/<job_id>/applications` | Applications for a recruiter’s job |
| PUT | `/applications/<id>/status` | Update application status |
| GET | `/applications/<id>/status-history` | View application status history |
| DELETE | `/applications/<id>` | Delete application |

---

## 🎯 Interview APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/applications/<id>/schedule` | Schedule interview |
| POST | `/interviews` | Create interview |
| GET | `/interviews` | List interviews |
| GET | `/interviews/<id>` | Interview details |
| PUT | `/interviews/<id>` | Update interview |
| DELETE | `/interviews/<id>` | Delete interview |

---

## 📄 Resume APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/resume/upload` | Upload resume |
| GET | `/resume/download` | Download resume |
| DELETE | `/resume/delete` | Delete resume |

---

## ❤️ Saved Job APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/saved-jobs/<job_id>` | Save a job |
| GET | `/saved-jobs` | View saved jobs |
| DELETE | `/saved-jobs/<job_id>` | Remove saved job |

---

## 👑 Admin APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/admin/dashboard` | Dashboard analytics |
| GET | `/admin/users` | List all users |
| GET | `/admin/jobs` | List all jobs |
| GET | `/admin/applications` | List all applications |

---

# 🔐 Authentication & Authorization

The API uses **JWT (JSON Web Tokens)** for secure authentication.

### User Roles

- 👨‍🎓 Candidate
- 🏢 Recruiter
- 👑 Admin

Protected endpoints require:

```
Authorization: Bearer <JWT_TOKEN>
```

Role-based decorators ensure that only authorized users can access protected resources.

---

# 🔒 Security Features

The backend includes several security mechanisms:

- JWT Authentication
- Role-Based Authorization
- Password Hashing
- Secure Password Reset
- Protected Routes
- Input Validation
- Duplicate Job Application Prevention
- Resume File Validation
- Secure File Upload Handling
- Environment Variable Configuration
- Database Migration Management
- Background Email Processing
- SQLAlchemy ORM Protection against SQL Injection

---

# 📧 Email Notifications

The system automatically sends email notifications for important events.

### Candidate Notifications

- Interview Scheduled
- Application Status Updated
- Password Reset

### Recruiter Notifications

- New Job Application Received

---

# 📊 Application Status Workflow

```
Applied
    │
    ▼
Shortlisted
    │
    ▼
Interview Scheduled
    │
 ┌──┴──┐
 ▼     ▼
Selected  Rejected
```

Each status update is recorded in the **Application Status History** table for tracking and audit purposes.

---

# 🗄️ Database Migrations

Alembic is used for version-controlled database migrations.

```bash
flask db init
```

```bash
flask db migrate -m "Initial migration"
```

```bash
flask db upgrade
```

---

# 🧪 API Testing

The backend has been tested using **Postman**.

### Tested Modules

- User Authentication
- JWT Authorization
- Candidate APIs
- Recruiter APIs
- Admin APIs
- Job CRUD Operations
- Resume Upload
- Resume Download
- Resume Delete
- Job Applications
- Saved Jobs
- Recently Viewed Jobs
- Interview Scheduling
- Interview Update
- Interview Delete
- Candidate Interview APIs
- Application Status Updates
- Application Status History
- Password Reset
- Email Notifications
- PostgreSQL Integration
- Render Deployment

---

# 📸 Screenshots

> Replace these placeholder images with your own screenshots.

### Home Page

![Home](screenshots/home.png)

### Candidate Dashboard

![Candidate Dashboard](screenshots/candidate_dashboard.png)

### Recruiter Dashboard

![Recruiter Dashboard](screenshots/recruiter_dashboard.png)

### Job Details

![Job Details](screenshots/job_details.png)

### Resume Upload

![Resume](screenshots/resume_upload.png)

### Interview Scheduling

![Interview](screenshots/interview_schedule.png)

---

# 📈 Project Statistics

### Backend

- RESTful APIs
- Modular Flask Architecture
- JWT Authentication
- PostgreSQL Database
- SQLAlchemy ORM
- Flask-Mail Integration
- Alembic Migrations
- Background Email Processing
- Role-Based Authorization

### Frontend

- React.js
- Vite
- Axios
- Responsive UI
- Dashboard Interfaces

---

# 🚀 Future Enhancements

- AI Resume Screening
- AI Candidate Ranking
- Resume Parsing
- Interview Feedback System
- Calendar Integration (Google Calendar)
- Real-Time Notifications
- Docker Support
- Swagger / OpenAPI Documentation
- Unit & Integration Testing
- CI/CD Pipeline
- Redis Caching
- Elasticsearch-based Job Search

---

# 👨‍💻 Developer

**P. Venumohan**

🎓 B.Tech – Computer Science & Data Science (2026)

💻 Python Backend Developer | Flask Developer

📍 Andhra Pradesh, India

### GitHub

https://github.com/Venumohan004

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">

## 🚀 Built with Flask • React • PostgreSQL • JWT • SQLAlchemy

### Made with ❤️ by P. Venumohan

</p>
