# Django Student Feedback System

## 📌 Overview
The Django Student Feedback System is a web-based application that allows students to submit feedback through a validated form.  
The application performs server-side validation using Django Forms and displays a success message after successful submission.

This project demonstrates form handling, custom validation, and template rendering in Django.

---

## 🚀 Concepts Used
- Django Forms
- Custom Field Validation (`clean_<fieldname>()`)
- Function-Based Views (FBV)
- Template Rendering
- CSRF Protection
- Conditional Template Display
- Django App Configuration (`apps.py`)
- Static Files Handling

---

## 📂 Project Structure

```
feedbackproject/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
│
├── feedbackproject/        # Main Project Folder (settings)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── testapp/                # Django App
│   ├── __pycache__/
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   └── testapp/
│       └── index.html
│
└── static/
    └── css/
        └── style.css
```

--- 

## ▶️ How to Run
- Install required packages `requirements.txt`
- Run the server `python manage.py runserver`
- Open in browser send request `http://127.0.0.1:8000/feedback`

---

## Author & Contact
<strong>Rajat Kumar Bal </strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a><br>
<div align='center'>
  Made With 💖 by <strong>Rajat</strong>
</div>
