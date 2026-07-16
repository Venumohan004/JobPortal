# 🚀 JobPortal – RESTful Backend API

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![JWT](https://img.shields.io/badge/JWT-Authentication-green?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![GitHub](https://img.shields.io/badge/Open%20Source-GitHub-black?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 💼 JobPortal Backend API

A **production-ready RESTful Job Portal Backend API** developed using:

- Python
- Flask
- MySQL
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

              MySQL

```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | Flask |
| Database | MySQL |
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

      ----------------------------

      |            |             |

 Candidate    Recruiter        Job

                  |

              Application

                  |

              SavedJob

                  |

        RecentlyViewedJob

```

---

# ⚙️ Installation

## 1. Clone Repository


```bash
git clone https://github.com/Venumohan004/jobPortal.git

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


MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DB=job_portal_day4


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


```
http://127.0.0.1:5000
```


---

# 📌 API Modules


| Module | Description |
|---|---|
| Authentication | Register, Login, Password Reset |
| Candidate | Profile, Resume, Applications |
| Recruiter | Jobs, Applications, Analytics |
| Admin | Dashboard, Reports |
| Jobs | CRUD, Search, Filter, Pagination |


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
| POST | `/apply` | Apply Job |
| GET | `/applications` | View Applications |
| POST | `/upload/resume` | Upload Resume |
| GET | `/admin/dashboard` | Admin Dashboard |


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


- Postman
- JWT Testing
- CRUD Testing
- Authentication Testing
- Authorization Testing


Example Response:


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

Made with ❤️ using Python, Flask & MySQL

</p>
