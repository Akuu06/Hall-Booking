# Hall Booking Management System

## 📌 Project Overview
This project is a **Hall Booking Management System** developed as part of the **Ascentech interview exercise**.

The system provides a RESTful backend to manage hall bookings, including creating, viewing, updating, and deleting booking records. The backend is built using **Django REST Framework**, with **PostgreSQL** as the database, and follows clean backend architecture and best practices.

All database operations are handled using **Django ORM** (no raw SQL).

---

## 🧰 Tech Stack

### Backend
- Python 3
- Django 6.0
- Django REST Framework
- PostgreSQL
- psycopg2-binary
- django-cors-headers

### Frontend
- React 


---

## ✨ Features
- RESTful API for hall booking management
- PostgreSQL database integration
- ORM-based CRUD operations
- Django Admin panel for data management
- Automatic timestamp handling (`created_at`, `updated_at`)
- Proper migration handling
- Clean and scalable backend structure

---

## 🗄️ Database Configuration (PostgreSQL)

### Database Details
- **Database Name:** `hall_booking_db`
- **User:** `halluser`
- **Password:** `hallpass`
- **Host:** `localhost`
- **Port:** `5432`

---

## 🚀 How to Run the Project (Step-by-Step)
## Project Setup & Execution Steps (macOS)

**Step 1: Install Dependencies**  
Run the following command to install all required Python packages:  
`pip install django djangorestframework psycopg2-binary django-cors-headers python-dotenv`

**Step 2: Install and Start PostgreSQL**  
Install PostgreSQL and start the service:  
`brew install postgresql`  
`brew services start postgresql`  

Verify installation:  
`psql --version`

**Step 3: Create Database and User**  
Open PostgreSQL shell:  
`psql postgres`  

Create database and user:  
`CREATE DATABASE hall_booking_db;`  
`CREATE USER halluser WITH PASSWORD 'hallpass';`  
`GRANT ALL PRIVILEGES ON DATABASE hall_booking_db TO halluser;`  
Exit shell:  
`\q`

**Step 4: Configure Django Database**  
Open the file:  
`backend/backend/settings.py`  

Update the database configuration:
`DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql','NAME': 'hall_booking_db','USER': 'halluser','PASSWORD': 'hallpass','HOST': 'localhost','PORT': '5432'}}`

**Step 5: Run Migrations**  
Apply database migrations:  
`python3 manage.py makemigrations`  
`python3 manage.py migrate`

**Step 6: Create Superuser**  
Create an admin user for Django Admin:  
`python3 manage.py createsuperuser`

**Step 7: Start Development Server**  
Run the Django server:  
`python3 manage.py runserver`

**Access URLs**  
Home: `http://127.0.0.1:8000/`  
Admin Panel: `http://127.0.0.1:8000/admin/`  
Bookings API: `http://127.0.0.1:8000/api/bookings/`

