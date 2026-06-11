<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg" width="80" height="80" alt="Django"/>

# E-Commerce Platform

**A production-grade Django e-commerce application with cart management, order tracking, and an admin dashboard.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=flat-square&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

[Features](#-features) · [Architecture](#-architecture) · [Tech Stack](#-tech-stack) · [Setup](#-setup) · [Security](#-security) · [Roadmap](#-roadmap)

</div>

---

## Overview

A scalable, modular e-commerce application built with **Django**, **Django REST Framework**, and **MySQL**, engineered to emulate real-world online retail workflows. The platform demonstrates practical implementation of RESTful service design, relational database modeling, secure authentication, and clean layered architecture.

---

## ✨ Features

| Module | Capabilities |
|---|---|
| **Authentication** | Secure registration & login, session management, role-based admin access, password hashing |
| **Product Catalog** | Category-based browsing, inventory tracking, stock monitoring, admin product management |
| **Cart & Checkout** | Persistent cart, quantity updates, order creation, checkout orchestration & confirmation |
| **Order Management** | Full order lifecycle, order history, user-specific records, admin monitoring |
| **Security** | CSRF protection, ORM-based SQL injection prevention, session handling, input validation |

---

## 🏗 Architecture

The platform follows a clean **layered architecture** promoting separation of concerns, maintainability, and scalability.

```
┌─────────────────────────────────────────────┐
│              Client Layer                   │
│         HTML · CSS · JavaScript             │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Presentation Layer                │
│    Django Templates · Views · URL Routing   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│            Application Layer                │
│  Auth Workflows · Order Processing Engine   │
│       Cart Management · Business Logic      │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Data Access Layer                 │
│              Django ORM                     │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           Persistence Layer                 │
│              MySQL Database                 │
└─────────────────────────────────────────────┘
```

---

## 💻 Tech Stack

<table>
  <tr>
    <td valign="top" width="33%">
      <b>Backend</b><br><br>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/><br>
      <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/><br>
      <img src="https://img.shields.io/badge/DRF-red?style=flat-square&logo=django&logoColor=white"/>
    </td>
    <td valign="top" width="33%">
      <b>Database</b><br><br>
      <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/><br>
      <img src="https://img.shields.io/badge/Django_ORM-092E20?style=flat-square&logo=django&logoColor=white"/>
    </td>
    <td valign="top" width="33%">
      <b>Frontend</b><br><br>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/><br>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/><br>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
    </td>
  </tr>
</table>

---

## 📁 Project Structure

```
ecommerce/
├── manage.py
├── requirements.txt
│
├── Main/                        # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── store/                       # Core application
    ├── models.py                # User · Product · Category · Order · Cart
    ├── views.py                 # Business logic
    ├── urls.py                  # URL routing
    ├── admin.py                 # Admin configuration
    ├── templates/
    │   ├── home.html
    │   ├── product_detail.html
    │   ├── cart.html
    │   ├── checkout.html
    │   └── order_history.html
    └── static/
        ├── css/
        └── js/
```

---

## ⚙️ Setup

### Prerequisites

- Python 3.8+
- MySQL Server 8.0+
- pip & virtualenv

### 1 · Clone the repository

```bash
git clone https://github.com/Sharathmh25/E-Commerce.git
cd E-Commerce
```

### 2 · Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure the database

Edit `Main/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> **Tip:** Use `python-dotenv` to keep credentials out of source control.

### 5 · Run migrations & create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6 · Start the server

```bash
python manage.py runserver
```

| Interface | URL |
|---|---|
| User Portal | http://127.0.0.1:8000/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🔒 Security

| Status | Feature |
|---|---|
| ✅ | CSRF protection enabled globally |
| ✅ | Password hashing via Django's authentication system |
| ✅ | SQL injection prevention through Django ORM |
| ✅ | Secure session management with signed cookies |
| ✅ | Input validation and sanitization |
| ⚠️ | Use environment variables for credentials — add `python-dotenv` |
| ⚠️ | Enable HTTPS and rate limiting before production |

---

## 🚀 Deployment Checklist

```bash
# 1. Disable debug mode
DEBUG = False

# 2. Set allowed hosts
ALLOWED_HOSTS = ['yourdomain.com']

# 3. Collect static files
python manage.py collectstatic

# 4. Serve with Gunicorn
gunicorn Main.wsgi:application --bind 0.0.0.0:8000
```

- [ ] Secrets moved to environment variables
- [ ] HTTPS enabled (Let's Encrypt)
- [ ] Nginx configured as reverse proxy
- [ ] Database backups scheduled
- [ ] `DEBUG = False` in settings

---

## 🗺 Roadmap

- [ ] Payment gateway integration (Stripe / PayPal)
- [ ] Email order confirmations with Celery
- [ ] Product reviews and ratings
- [ ] Wishlist feature
- [ ] Advanced search with Elasticsearch
- [ ] REST / GraphQL API
- [ ] JWT Authentication
- [ ] Redis caching layer
- [ ] Docker containerisation
- [ ] CI/CD with GitHub Actions
- [ ] Kubernetes deployment
- [ ] Analytics dashboard
- [ ] Cloud deployment on AWS

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/your-feature

# 3. Commit your changes
git commit -m "Add your-feature"

# 4. Push to the branch
git push origin feature/your-feature

# 5. Open a Pull Request
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by [Sharath M H](https://github.com/Sharathmh25)

⭐ Star this repo if you found it useful!

</div>
