# 🚀 Job Portal Backend

A RESTful Job Portal Backend built using **Python, Flask, MySQL, SQLAlchemy, and JWT Authentication**. This project provides secure authentication, role-based authorization, job management, resume management, saved jobs, and job application features.

---

## 📌 Features

### 👤 User Authentication

* User Registration
* User Login
* JWT Authentication
* Password Hashing using bcrypt
* Protected Routes

### 🔐 Role-Based Authorization

* Candidate
* Recruiter
* Admin
* Recruiter-only Job Management
* Candidate-only Job Applications

### 💼 Job Management

* Create Job
* View All Jobs
* Update Job
* Delete Job
* Search Jobs
* Filter Jobs by Company
* Filter Jobs by Location
* Filter Jobs by Salary
* Pagination

### 📄 Resume Management

* Upload Resume
* View Resume
* Update Resume
* Delete Resume

### ⭐ Saved Jobs

* Save Job
* View Saved Jobs
* Remove Saved Job

### 📝 Job Applications

* Apply for Job
* Prevent Duplicate Applications
* View Applications
* Delete Own Application
* Recruiter View Applications
* Update Application Status

---

# 🛠️ Tech Stack

* Python
* Flask
* MySQL
* SQLAlchemy
* Flask-JWT-Extended
* Flask-CORS
* bcrypt
* Postman
* Git
* GitHub

---

# 📂 Project Structure

```text
backend/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── job.py
│   ├── resume.py
│   ├── saved_job.py
│   └── application.py
│
├── routes/
│   ├── auth.py
│   ├── jobs.py
│   ├── resume.py
│   ├── saved_jobs.py
│   └── application.py
│
└── migrations/
```

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

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask server

```bash
python app.py
```

---

# 🔑 Authentication

This project uses **JWT (JSON Web Token)**.

Protected APIs require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 📮 Main APIs

## Authentication

* POST `/register`
* POST `/login`
* GET `/profile`

## Jobs

* POST `/jobs`
* GET `/jobs`
* PUT `/jobs/<id>`
* DELETE `/jobs/<id>`
* GET `/jobs/search`
* GET `/jobs/company/<company>`
* GET `/jobs/location/<location>`
* GET `/jobs/salary/<salary>`
* GET `/jobs/page`

## Resume

* POST `/resume`
* GET `/resume`
* PUT `/resume/<id>`
* DELETE `/resume/<id>`

## Saved Jobs

* POST `/saved-jobs`
* GET `/saved-jobs`
* DELETE `/saved-jobs/<id>`

## Applications

* POST `/apply`
* GET `/applications`
* DELETE `/applications/<id>`
* GET `/jobs/<job_id>/applications`
* PUT `/applications/<id>/status`

---

# 🧪 Tested Using

* Postman
* MySQL
* Flask Development Server

---

# 📚 What I Learned

* Flask REST API Development
* SQLAlchemy ORM
* MySQL Database Integration
* JWT Authentication
* Role-Based Authorization
* CRUD Operations
* API Testing using Postman
* Password Hashing using bcrypt
* Pagination
* Search & Filtering
* Git & GitHub Workflow

---

# 🚧 Project Status

✅ Authentication Completed

✅ Role-Based Authorization Completed

✅ Job Management Completed

✅ Resume Management Completed

✅ Saved Jobs Completed

✅ Job Application Management Completed

🟡 Recruiter Dashboard (In Progress)

🟡 Admin Dashboard (In Progress)

🟡 Deployment (Pending)

---

# 👨‍💻 Author

**Pilli Venumohan**

* GitHub: https://github.com/Venumohan004
* LinkedIn: https://linkedin.com/in/venumohan-p-522017346

---

⭐ If you like this project, feel free to star the repository.
