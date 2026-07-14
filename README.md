# 🚀 JobPortal – RESTful Backend API

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge\&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge\&logo=mysql)
![JWT](https://img.shields.io/badge/JWT-Authentication-green?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![GitHub](https://img.shields.io/badge/Open%20Source-GitHub-black?style=for-the-badge\&logo=github)

</p>

A **production-ready RESTful Job Portal Backend** built using **Python, Flask, MySQL, SQLAlchemy, JWT Authentication, Flask-Mail, and Flask-Migrate**.

This project provides a complete backend solution for an online job portal where:

* 👨‍🎓 Candidates can create profiles, upload resumes, search and apply for jobs.
* 🏢 Recruiters can post jobs, manage applications, and track hiring.
* 👑 Administrators can monitor users, jobs, applications, and platform analytics.

---

## 🌟 Highlights

- 🔐 JWT Authentication & Authorization
- 👨‍🎓 Candidate Portal
- 🏢 Recruiter Portal
- 👑 Admin Dashboard
- 📄 Resume Upload & Download
- ❤️ Saved Jobs
- 👀 Recently Viewed Jobs
- 📊 Analytics Dashboard
- 📧 Email Integration
- 🔍 Job Search & Filtering
- 📑 Pagination & Sorting
- 🛡️ Role-Based Access Control


# ✨ Features

## 🔐 Authentication

* User Registration
* Secure Login
* JWT Authentication
* Role-Based Authorization
* Forgot Password
* Password Reset via Email
* Protected Routes
* Password Hashing

---

## 👨‍🎓 Candidate Features

* Create Profile
* Update Profile
* View Profile
* Upload Resume
* Download Resume
* Delete Resume
* Apply for Jobs
* View Applied Jobs
* Save Jobs
* Remove Saved Jobs
* Recently Viewed Jobs
* Candidate Dashboard
* Application Status Tracking
* Job Recommendations

---

## 🏢 Recruiter Features

* Recruiter Profile
* Company Profile
* Create Job
* Update Job
* Delete Job
* View Posted Jobs
* View Applications
* Accept Candidates
* Reject Candidates
* Shortlist Candidates
* Recruiter Dashboard
* Recruiter Analytics

---

## 👑 Admin Features

* Dashboard
* View All Users
* View All Recruiters
* View All Candidates
* View All Jobs
* View All Applications
* Delete Users
* Delete Jobs
* Reports
* Platform Analytics

---

## 💼 Job Features

* Create Job
* Update Job
* Delete Job
* Search Jobs
* Filter Jobs
* Sort Jobs
* Pagination
* Company-wise Search
* Location-wise Search
* Salary Filtering
* Experience Filtering
* Skills Filtering

---

## 📄 Resume Management

* Resume Upload
* Resume Download
* Resume Delete
* PDF Validation
* Secure Storage

---

## ❤️ Saved Jobs

* Save Job
* View Saved Jobs
* Remove Saved Jobs

---

## 👀 Recently Viewed Jobs

* Track Viewed Jobs
* View Recently Viewed Jobs

---

## 📊 Dashboards

### Candidate Dashboard

* Applied Jobs
* Saved Jobs
* Selected Applications
* Rejected Applications

### Recruiter Dashboard

* Jobs Posted
* Applications Received
* Candidate Statistics

### Admin Dashboard

* Total Users
* Total Recruiters
* Total Candidates
* Total Jobs
* Total Applications

---

# 🛠 Tech Stack

* Python
* Flask
* MySQL
* SQLAlchemy
* Flask-JWT-Extended
* Flask-Mail
* Flask-Migrate
* Flask-CORS
* Alembic
* REST API
* JWT Authentication
* Postman
* Git
* GitHub

---

# 📂 Project Structure

```text
backend/
│
├── models/
├── routes/
├── services/
├── migrations/
├── static/
├── templates/
├── uploads/
├── utils/
├── instance/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Venumohan004/jobPortal.git
```

```bash
cd jobPortal
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret_key

MYSQL_HOST=localhost

MYSQL_USER=root

MYSQL_PASSWORD=your_password

MYSQL_DB=job_portal_day4

MAIL_SERVER=smtp.gmail.com

MAIL_PORT=587

MAIL_USERNAME=your_email@gmail.com

MAIL_PASSWORD=your_app_password

MAIL_USE_TLS=True

MAIL_USE_SSL=False

```
 
---

## 5️⃣ Database Migration

```bash
flask db init
```

```bash
flask db migrate
```

```bash
flask db upgrade
```

---

## 6️⃣ Run Server

```bash
python app.py
```

Server URL

```text
http://127.0.0.1:5000
```

---

# 📌 API Modules

### 🔐 Authentication

* Register
* Login
* Forgot Password
* Reset Password

### 👨‍🎓 Candidate APIs

* Candidate Profile
* Apply Job
* Resume
* Saved Jobs
* Recently Viewed Jobs
* Dashboard

### 🏢 Recruiter APIs

* Recruiter Profile
* Company Profile
* Job CRUD
* Applications
* Dashboard
* Analytics

### 👑 Admin APIs

* Dashboard
* Users
* Jobs
* Applications
* Reports

### 💼 Job APIs

* CRUD
* Search
* Filter
* Sort
* Pagination

---

# 🔒 Security

* JWT Authentication
* Password Hashing
* Role-Based Access Control
* Protected Endpoints
* Input Validation
* Secure Password Reset Tokens
* File Validation

---

# 🧪 API Testing

All REST APIs were tested using **Postman**.

Example Response

```json
{
    "message": "Login Successful",
    "token": "JWT_TOKEN"
}
```

---

# 🚀 Future Enhancements

* AI Resume Screening
* AI Candidate Ranking
* Email Notifications
* Interview Scheduling Improvements
* Docker Deployment
* Swagger/OpenAPI Documentation
* Unit Testing
* CI/CD Pipeline
* Redis Caching

---

# 📷 Project Screenshots

You can add:

* Login API
* Register API
* Candidate Dashboard
* Recruiter Dashboard
* Admin Dashboard
* Postman Collection
* Database ER Diagram

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 👨‍💻 Developer

**P. Venumohan**

🎓 B.Tech – Computer Science & Data Science

💻 Python Backend & REST API Developer

📍 Andhra Pradesh, India

🔗 GitHub: https://github.com/Venumohan004

---

# ⭐ Show Your Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support helps and motivates me to build more open-source projects.

---

Made with ❤️ using Python & Flask by **P. Venumohan**

---

# 📄 License

This project is licensed under the **MIT License**. 
