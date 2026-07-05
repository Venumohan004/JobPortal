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
│   └── job.py
│
├── routes/
│   ├── auth.py
│   ├── candidate.py
│   ├── recruiter.py
│   └── jobs.py
│
└── utils/
```

## ✅ Features Completed

### Day 1

* Project Setup
* Flask Configuration
* MySQL Database Connection
* SQLAlchemy Setup

### Day 2

* User Registration
* User Login
* JWT Authentication

### Day 3

* Candidate Profile
* View Candidate Profile
* Update Candidate Profile

### Day 4

* Recruiter Profile
* Create Job
* Get All Jobs
* Get Job by ID
* Update Job
* Delete Job

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

## 🛠️ Tools Used

* Visual Studio Code
* Postman
* MySQL Workbench / MySQL Command Line
* Git
* GitHub

## ▶️ Run the Project

1. Clone the repository

```bash
git clone https://github.com/Venumohan004/JobPortal.git
```

2. Navigate to the project

```bash
cd JobPortal/backend
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure the `.env` file

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DB_HOST=localhost
DB_PORT=3306
DB_NAME=job_portal_day4
DB_USER=root
DB_PASSWORD=your_password
```

5. Run the application

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000/
```

## 🚀 Upcoming Features

* Job Application Module
* Resume Upload
* Saved Jobs
* Admin Panel
* Search & Filter Jobs

## 👨‍💻 Author

**Pilli Venumohan**

GitHub: https://github.com/Venumohan004
