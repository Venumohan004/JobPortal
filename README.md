# Job Portal Backend

A production-ready **RESTful Job Portal Backend** built using **Python, Flask, MySQL, SQLAlchemy, JWT Authentication, and Flask-Mail**.

## 🚀 Tech Stack

* Python
* Flask
* MySQL
* SQLAlchemy
* Flask-JWT-Extended
* Flask-Mail
* Flask-CORS
* JWT Authentication
* Postman
* Git & GitHub

---

# 📂 Project Structure

```text
backend/
│
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── user.py
│   ├── company.py
│   ├── job.py
│   └── application.py
│
├── routes/
│   ├── auth.py
│   ├── company.py
│   ├── jobs.py
│   ├── applications.py
│   └── admin.py
│
├── utils/
│   └── email_service.py
│
├── middleware/
├── migrations/
├── .env
├── requirements.txt
└── README.md
```

---

# ✨ Features Implemented

## ✅ User Authentication

* User Registration
* User Login
* Password Hashing
* JWT Authentication
* Protected Routes

---

## ✅ Role-Based Access Control (RBAC)

* Admin
* Employer
* Job Seeker

Each role has access only to authorized APIs.

---

## ✅ Company Management

* Create Company
* Update Company
* Delete Company
* View Company Details

---

## ✅ Job Management

* Create Job
* Update Job
* Delete Job
* View All Jobs
* View Single Job

---

## ✅ Job Applications

* Apply for Job
* View Applied Jobs
* Employer View Applications
* Prevent Duplicate Applications

---

## ✅ Admin APIs

* View All Users
* View All Companies
* View All Jobs
* Manage Platform Data

---

## ✅ Email Integration

* Welcome Email on Successful Registration
* Gmail SMTP Configuration
* Flask-Mail Integration

---

# 🔒 Security Features

* Password Hashing
* JWT Token Authentication
* Role-Based Authorization
* Environment Variables (.env)
* Secure Email Configuration

---

# 🛠 Database

* MySQL
* SQLAlchemy ORM

Main Tables:

* Users
* Companies
* Jobs
* Applications

---

# 📬 API Testing

All APIs are tested using **Postman**.

Example APIs:

* Register User
* Login User
* Create Company
* Create Job
* Apply Job
* View Applications
* Admin Dashboard APIs

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

Go to the project folder:

```bash
cd JobPortal/backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the `.env` file:

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

Run the application:

```bash
python app.py
```

---

# 📌 Current Progress

* ✅ Day 1 – Flask Project Setup
* ✅ Day 2 – Database Configuration
* ✅ Day 3 – User Model
* ✅ Day 4 – User Registration
* ✅ Day 5 – Login & JWT Authentication
* ✅ Day 6 – CRUD APIs
* ✅ Day 7 – Role-Based Access Control
* ✅ Day 8 – Company Management
* ✅ Day 9 – Job Management
* ✅ Day 10 – Job Application System
* ✅ Day 11 – Admin Dashboard APIs
* ✅ Day 12 – Flask-Mail Setup
* ✅ Day 13 – Welcome Email System

---

# 🚀 Upcoming Features

* Forgot Password
* Password Reset via Email
* Email Verification
* Resume Upload
* Job Search & Filters
* Pagination
* API Documentation (Swagger)
* Docker Support
* Deployment

---

# 👨‍💻 Author

**P Venumohan**

* GitHub: https://github.com/Venumohan004

---

## ⭐ If you like this project, don't forget to Star the repository!
