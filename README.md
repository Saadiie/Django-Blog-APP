# 📝 InkWell — Full-Stack Django Blog Platform

A full-stack blog application built with Python & Django, featuring user authentication, 
author-only post management, featured image uploads, and searchable, paginated content browsing.

---

## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **Framework:** Django 6.0.5
- **Database:** SQLite3 (built-in, no setup needed)
- **Frontend:** HTML, CSS (Django Templates)

---

## ✨ Features

- User registration, login, and logout via Django's Authentication System
- CRUD operations for blog posts with author-only edit permissions
- Featured image upload for blog posts
- Search and pagination for content browsing
- Responsive frontend with reusable Django template structure

---

## ⚙️ Setup & Installation

### Step 1 — Clone the repository
    git clone https://github.com/Saadiie/Django-Blog-APP.git
    cd Django-Blog-APP

### Step 2 — Create & Activate Virtual Environment
    python -m venv venv

    # Fix execution policy (Windows only - one time per terminal session)
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

    # Activate venv
    venv\Scripts\activate

You should see `(venv)` appear in your terminal.

### Step 3 — Install Dependencies
    pip install -r requirements.txt

### Step 4 — Navigate to project root
    cd myblog

### Step 5 — Run Migrations
    python manage.py makemigrations
    python manage.py migrate

### Step 6 — Create Admin User (optional)
    python manage.py createsuperuser

### Step 7 — Start the Server
    python manage.py runserver

Visit `http://127.0.0.1:8000/blogs/` in your browser. ✅

---

## 🌐 Available URLs

| URL | Method | Description |
|---|---|---|
| `/blogs/` | GET | List all blog posts (search + pagination) |
| `/blogs/create/` | GET / POST | Create a new blog post (login required) |
| `/blogs/<id>/` | GET | View a single blog post |
| `/blogs/<id>/edit/` | GET / POST | Edit a blog post (author only) |
| `/accounts/register/` | GET / POST | User registration |
| `/accounts/login/` | GET / POST | User login |
| `/accounts/logout/` | POST | User logout |
| `/admin/` | GET | Django admin panel |

---

## 🗄️ Database

This project uses **SQLite3**, Django's default database. The `db.sqlite3` file is automatically created inside `myblog/` when you run migrations.

---

## 👤 Author

**Saad Mehmood** — Python/Django Developer