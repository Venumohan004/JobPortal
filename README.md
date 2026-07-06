# Job Portal Backend

A RESTful Job Portal Backend built using **Python, Flask, MySQL, SQLAlchemy, JWT Authentication, HTML, CSS, and Bootstrap**.

---

## 🚀 Tech Stack

- Python
- Flask
- MySQL
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-CORS
- HTML
- CSS
- Bootstrap
- JavaScript
- Postman
- Git & GitHub

---

## 📂 Project Structure

```text
backend/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── models/
│   ├── user.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── job.py
│   ├── application.py
│   ├── resume.py
│   └── saved_job.py
│
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── jobs.py
│   ├── application.py
│   ├── resume.py
│   └── saved_jobs.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── jobs.html
│   ├── profile.html
│   ├── add_job.html
│   ├── edit_job.html
│   ├── job_details.html
│   └── 404.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── migrations/
```

---

# ✅ Features Completed

### 📅 Day 1

- Project Setup
- Flask Configuration
- MySQL Database Connection
- SQLAlchemy Setup
- Git & GitHub Repository

---

### 📅 Day 2

- User Model
- User Registration
- User Login
- Password Hashing (bcrypt)
- JWT Authentication

---

### 📅 Day 3

- Candidate Profile Model
- Create Candidate Profile
- View Candidate Profile
- Update Candidate Profile

---

### 📅 Day 4

- Recruiter Profile
- Create Recruiter
- Job Model
- Create Job API
- View Jobs API
- Update Job API
- Delete Job API

---

### 📅 Day 5

- Apply for Job
- View Applications
- Delete Application
- Recruiter View Applications
- Protected Routes using JWT

---

### 📅 Day 6

- Resume Upload Module
- View Resume
- Update Resume
- Delete Resume
- Saved Jobs Module
- Save Job
- View Saved Jobs
- Delete Saved Job

---

### 📅 Day 7

- Search Jobs
- Filter Jobs by Company
- Filter Jobs by Location
- Filter Jobs by Salary
- Pagination
- Improved API Responses
- MySQL Migration Support

---

### 📅 Day 8

- Bootstrap Frontend Setup
- Home Page
- Register Page
- Login Page
- Dashboard Page
- Profile Page
- Jobs Page
- Add Job Page
- Edit Job Page
- Job Details Page
- 404 Error Page
- Static CSS & JavaScript
- Registration Connected with MySQL
- Backend & Frontend Integration Started

---

# 📌 API Endpoints

## Authentication

- POST `/register`
- POST `/login`
- GET `/profile`

---

## Candidate

- POST `/candidate/profile`
- GET `/candidate/profile`
- PUT `/candidate/profile`

---

## Recruiter

- POST `/recruiter`

---

## Jobs

- POST `/jobs`
- GET `/jobs`
- PUT `/jobs/<id>`
- DELETE `/jobs/<id>`
- GET `/jobs/search`
- GET `/jobs/company/<company>`
- GET `/jobs/location/<location>`
- GET `/jobs/salary/<salary>`
- GET `/jobs/page`

---

## Applications

- POST `/apply`
- GET `/applications`
- DELETE `/applications/<id>`
- GET `/jobs/<job_id>/applications`

---

## Resume

- POST `/resume`
- GET `/resume/<candidate_id>`
- PUT `/resume/<id>`
- DELETE `/resume/<id>`

---

## Saved Jobs

- POST `/save-job`
- GET `/saved-jobs/<candidate_id>`
- DELETE `/saved-jobs/<id>`

---

# 🛠️ Tools Used

- Visual Studio Code
- MySQL Workbench
- MySQL Server
- Postman
- Git
- GitHub
- Bootstrap 5

---

# ▶️ Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

## 2. Go to Project Folder

```bash
cd JobPortal/backend
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret_key

DB_HOST=localhost

DB_PORT=3306

DB_NAME=job_portal_day4

DB_USER=root

DB_PASSWORD=your_password
```

## 5. Run the Application

```bash
python app.py
```

Server URL

```text
http://127.0.0.1:5000/
```

---

# 🚀 Upcoming Features

- Complete Login Frontend
- Display Jobs using HTML & JavaScript
- Recruiter Dashboard
- Candidate Dashboard
- Profile Management UI
- Admin Dashboard
- Email Verification
- Password Reset
- Deploy on Render
- Responsive UI Improvements

---

# 👨‍💻 Author

**Pilli Venumohan**

- GitHub: https://github.com/Venumohan004
- LinkedIn: https://linkedin.com/in/venumohan-p-522017346

---

## ⭐ Project Status

**Current Version:** Day 8 Completed ✅

**Backend:** 95% Completed

**Frontend:** In Progress 🚧
