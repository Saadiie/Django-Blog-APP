# 📝 Django Blog App

A simple blog application built with Python & Django that allows you to create, view, and list blog posts using SQLite as the default database.

---

## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **Framework:** Django 6.0.5
- **Database:** SQLite3 (built-in, no setup needed)
- **Frontend:** HTML, CSS (Django Templates)

---

## 📁 Project Structure

```
BLOGS/
├── myblog/                   ← project root (run all commands from here)
│   ├── blog/                 ← blog app
│   │   ├── migrations/       ← auto-generated database migrations
│   │   ├── templates/
│   │   │   └── blog/
│   │   │       ├── list.html      ← all blogs page
│   │   │       ├── detail.html    ← single blog page
│   │   │       └── create.html    ← create blog form
│   │   ├── __init__.py
│   │   ├── admin.py          ← register models to admin panel
│   │   ├── apps.py           ← app configuration
│   │   ├── models.py         ← Blog database model
│   │   ├── urls.py           ← blog URL routes
│   │   └── views.py          ← list, get, create logic
│   ├── config/               ← project settings package
│   │   ├── __init__.py
│   │   ├── settings.py       ← all project configuration
│   │   ├── urls.py           ← root URL configuration
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── db.sqlite3            ← SQLite database (auto-created)
│   └── manage.py             ← Django command-line utility
├── venv/                     ← virtual environment (do not edit)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### Step 1 — Clone the repository

```cmd
git clone https://github.com/Saadiie/Django-Blog-APP.git
cd Django-Blog-APP
```

### Step 2 — Create & Activate Virtual Environment

```powershell
python -m venv venv

# Fix execution policy (Windows only - one time per terminal session)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# Activate venv
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal.

### Step 3 — Install Dependencies

```cmd
pip install django
```

Or if a `requirements.txt` exists:

```cmd
pip install -r requirements.txt
```

### Step 4 — Navigate to project root

```cmd
cd myblog
```

### Step 5 — Run Migrations

Creates all database tables in SQLite automatically:

```cmd
python manage.py makemigrations
python manage.py migrate
```

### Step 6 — Create Admin User (optional)

```cmd
python manage.py createsuperuser
```

Enter your preferred username and password when prompted.

### Step 7 — Start the Server

```cmd
python manage.py runserver
```

Visit `http://127.0.0.1:8000/blogs/` in your browser. ✅

---

## 🌐 Available URLs

| URL | Method | Description |
|-----|--------|-------------|
| `/blogs/` | GET | List all blog posts |
| `/blogs/create/` | GET / POST | Create a new blog post |
| `/blogs/<id>/` | GET | View a single blog post |
| `/admin/` | GET | Django admin panel |

---

## 📌 Every Time You Return to the Project

```powershell
# 1. Activate venv (from BLOGS/ folder)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\activate

# 2. Navigate to project root
cd myblog

# 3. Start server
python manage.py runserver
```

---

## 🗄️ Database

This project uses **SQLite3** which is Django's default database. No extra installation or configuration needed. The `db.sqlite3` file is automatically created inside `myblog/` when you run migrations.

---

## ⚠️ Important Notes

- Always include `{% csrf_token %}` inside every HTML `<form method="POST">` — without it Django returns a **403 Forbidden** error. This is Django's built-in security against Cross-Site Request Forgery attacks.
- Always run commands from inside the `myblog/` folder where `manage.py` lives.
- After any changes to `models.py`, always run `makemigrations` then `migrate`.
- Never share your `SECRET_KEY` from `settings.py` publicly.

---

## 🧪 Quick Test Checklist

- [ ] `(venv)` is showing in terminal
- [ ] Inside `myblog/` folder
- [ ] Migrations have been run successfully
- [ ] Server running at `http://127.0.0.1:8000`
- [ ] `/blogs/` shows list page without errors
- [ ] `/blogs/create/` shows the form
- [ ] After submitting form, blog appears in `/blogs/`
- [ ] `/admin/` panel is accessible

---

## 👤 Author

**Saad** -- **Python Developer**
