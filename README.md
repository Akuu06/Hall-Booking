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

### ✅ Step 1: Clone the Repository
```bash
git clone <your-github-repo-url>
cd hall-booking-system/backend

##✅ Step 2: Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

