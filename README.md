# 🏥 Healthcare Backend System (Django + DRF + PostgreSQL)

## 📌 Project Overview

This project is a backend system for a healthcare application built
using **Django**, **Django REST Framework**, and **PostgreSQL**.\
It allows users to register, log in securely using JWT authentication,
and manage patient and doctor records.

The system provides RESTful APIs for authentication, patient management,
doctor management, and patient-doctor mapping.

---

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Secure REST APIs using Django REST Framework
- PostgreSQL Database Integration
- Patient Management (CRUD)
- Doctor Management (CRUD)
- Assign Doctors to Patients
- JWT-based Authorization
- Environment Variables for Security
- Proper Project Structure & Validation

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Simple JWT (Authentication)
- dotenv (Environment Variables)
- Postman (API Testing)

---

## 📂 Project Structure

healthcare-backend/ │ ├── healthcare/ │ ├── settings.py │ ├── urls.py │
├── accounts/ ├── patients/ ├── doctors/ ├── mappings/ │ ├── .env ├──
manage.py └── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd healthcare-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate       # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install djangorestframework-simplejwt
pip install python-dotenv
```

### 4️⃣ PostgreSQL Setup

Create database in PostgreSQL:

```sql
CREATE DATABASE healthcare_db;
```

### 5️⃣ Create .env file

Create `.env` in root folder:

    SECRET_KEY=your_secret_key
    DEBUG=True
    DB_NAME=healthcare_db
    DB_USER=postgres
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
    DB_PORT=5432

---

## 🧱 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Run Server

```bash
python manage.py runserver
```

Server runs at:

    http://127.0.0.1:8000/

---

## 🔐 Authentication APIs

### Register

POST `/api/auth/register/`

Body:

    {
      "username": "aryan",
      "email": "aryan@email.com",
      "password": "123456"
    }

### Login

POST `/api/auth/login/`

Returns JWT token.

Add token in headers:

    Authorization: Bearer <token>

---

## 🧑‍⚕️ Patient APIs

Method Endpoint Description

---

POST /api/patients/ Add patient
GET /api/patients/ Get all patients
GET /api/patients/`<id>`{=html}/ Get patient
PUT /api/patients/`<id>`{=html}/ Update
DELETE /api/patients/`<id>`{=html}/ Delete

---

## 👨‍⚕️ Doctor APIs

Method Endpoint Description

---

POST /api/doctors/ Add doctor
GET /api/doctors/ Get all doctors
PUT /api/doctors/`<id>`{=html}/ Update
DELETE /api/doctors/`<id>`{=html}/ Delete

---

## 🔗 Mapping APIs

Method Endpoint Description

---

POST /api/mappings/ Assign doctor to patient
GET /api/mappings/ View all mappings
GET /api/mappings/`<patient_id>`{=html}/ Doctors for patient
DELETE /api/mappings/`<id>`{=html}/ Remove mapping

---

## 🧪 Testing

Use Postman or any API client.

Steps: 1. Register user 2. Login → get token 3. Add token in
Authorization header 4. Test all APIs

---

## 🛡️ Security Features

- JWT Authentication
- Authenticated endpoints
- Environment variables for sensitive data
- User-specific patient access
- Validation & error handling

---

## 📚 Learning Outcomes

- Django REST API development
- PostgreSQL integration
- JWT authentication
- Secure backend design
- API testing with Postman

---

## 👨‍💻 Author

Aryan Manchanda\
B.Tech CSE (3rd Year)

---

## ⭐ Submission Notes

This project was developed as part of a Django backend assignment to
demonstrate REST API development, authentication, and database
management using PostgreSQL.
