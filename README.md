# 📝 Django Blog App

A simple blog application built with Django that allows you to create, view, and list blog posts using SQLite as the database.

---

## 🛠️ Tech Stack

- **Python** 3.14+
- **Django** 6.0.5
- **Database** SQLite3 (built-in, no setup needed)

---

## 📁 Project Structure

```
Blogs/
├── config/                  ← run all commands from here
│   ├── blog/                ← blog app
│   │   ├── migrations/      ← database migration files
│   │   ├── templates/
│   │   │   └── blog/
│   │   │       ├── list.html      ← all blogs page
│   │   │       ├── detail.html    ← single blog page
│   │   │       └── create.html    ← create blog form
│   │   ├── models.py        ← Blog database model
│   │   ├── views.py         ← list, get, create logic
│   │   ├── urls.py          ← blog URL routes
│   │   └── admin.py         ← admin panel config
│   ├── config/              ← project settings
│   │   ├── settings.py
│   │   └── urls.py
│   ├── db.sqlite3           ← SQLite database (auto-created)
│   └── manage.py
└── venv/                    ← virtual environment
```

---

## ⚙️ Setup & Installation

### Step 1 — Clone or open the project in VSCode

Open the `Blogs` folder in VSCode.

### Step 2 — Activate Virtual Environment

Open the terminal in VSCode (`Ctrl + backtick`) and run:

```powershell
# Fix execution policy (only needed once)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# Activate venv
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal.

### Step 3 — Navigate to the project folder

```cmd
cd config
```

### Step 4 — Install Dependencies

```cmd
pip install django
```

Or if a `requirements.txt` exists:

```cmd
pip install -r requirements.txt
```

### Step 5 — Run Migrations

This creates the database tables in SQLite:

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

---

## 🌐 Available URLs

| URL | Method | Description |
|-----|--------|-------------|
| `http://127.0.0.1:8000/blogs/` | GET | List all blog posts |
| `http://127.0.0.1:8000/blogs/create/` | GET / POST | Create a new blog post |
| `http://127.0.0.1:8000/blogs/<id>/` | GET | View a single blog post |
| `http://127.0.0.1:8000/admin/` | GET | Django admin panel |

---

## 📌 Every Time You Return to the Project

Run these commands every time you open the project:

```powershell
# 1. Activate venv (from Blogs/ folder)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
venv\Scripts\activate

# 2. Go into project folder
cd config

# 3. Start server
python manage.py runserver
```

---

## 🗄️ Database

This project uses **SQLite3** which is Django's default database. No extra installation or configuration is needed. The database file `db.sqlite3` is automatically created inside the `config/` folder when you run migrations.

---

## ⚠️ Important Notes

- Always include `{% csrf_token %}` inside every HTML `<form>` that uses `method="POST"` — otherwise Django will return a **403 Forbidden** error.
- Never run `python manage.py runserver` from the `Blogs/` root folder — always `cd config` first.
- After changing `models.py`, always run `makemigrations` and `migrate` again.

---

## 🧪 Quick Test Checklist

- [ ] `venv` is activated (`(venv)` shows in terminal)
- [ ] Inside `config/` folder
- [ ] Migrations have been run
- [ ] Server is running at `http://127.0.0.1:8000`
- [ ] Can visit `/blogs/` without errors
- [ ] Can create a blog at `/blogs/create/`
- [ ] Created blog appears at `/blogs/`

---

## 👤 Author

**Saad** — Grayphite Tasks
