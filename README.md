# Job Portal Backend

A RESTful Job Portal Backend built using **Python, Flask, MySQL, SQLAlchemy, and JWT Authentication**.

## 🚀 Tech Stack

* Python
* Flask
* MySQL
* SQLAlchemy
* Flask-JWT-Extended
* Flask-CORS
* Postman
* Git & GitHub

---

## 📂 Project Structure

```text
backend/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── user.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── job.py
│   └── application.py
│
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   ├── jobs.py
│   └── application.py
│
└── utils/
```

---

## ✅ Features Completed

### 📅 Day 1

* Project Setup
* Flask Configuration
* MySQL Database Connection
* SQLAlchemy Setup

### 📅 Day 2

* User Registration
* User Login
* JWT Authentication

### 📅 Day 3

* Candidate Profile
* View Candidate Profile
* Update Candidate Profile

### 📅 Day 4

* Recruiter Profile
* Create Job
* Get All Jobs
* Get Job by ID
* Update Job
* Delete Job

### 📅 Day 5

* Apply for Job
* View All Applications
* Delete Application
* Recruiter View Applications

---

## 📌 API Endpoints

### Authentication

* POST `/register`
* POST `/login`
* GET `/profile`

### Candidate

* POST `/candidate/profile`
* GET `/candidate/profile`
* PUT `/candidate/profile`

### Recruiter

* POST `/recruiter`

### Jobs

* POST `/jobs`
* GET `/jobs`
* GET `/jobs/<id>`
* PUT `/jobs/<id>`
* DELETE `/jobs/<id>`

### Applications

* POST `/apply`
* GET `/applications`
* DELETE `/applications/<id>`
* GET `/jobs/<job_id>/applications`

---

## 🛠️ Tools Used

* Visual Studio Code
* Postman
* MySQL
* Git
* GitHub

---

## ▶️ Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

### 2. Go to Project Folder

```bash
cd JobPortal/backend
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DB_HOST=localhost
DB_PORT=3306
DB_NAME=job_portal_day4
DB_USER=root
DB_PASSWORD=your_password
```

### 5. Run the Application

```bash
python app.py
```

Server URL:

```text
http://127.0.0.1:5000/
```

---

## 🚀 Upcoming Features

* Resume Upload Module
* Saved Jobs
* Admin Dashboard
* Search & Filter Jobs
* Email Notifications

---

## 👨‍💻 Author

**Pilli Venumohan**

* GitHub: https://github.com/Venumohan004
* LinkedIn: https://linkedin.com/in/venumohan-p-522017346
