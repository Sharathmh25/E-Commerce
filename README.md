# 🛒 E-Commerce Web Application

A modern E-Commerce web application built using **Django** and **MySQL**, featuring user registration, authentication, and a clean UI for managing an online store.

---

## 🚀 Features

* 👤 User Registration & Login System
* 🔐 Secure Authentication (CSRF Protection enabled)
* 🛍️ Product Management (Add / View Products)
* 🎨 Responsive UI with modern design
* ⚡ Backend powered by Django ORM
* 🗄️ MySQL Database Integration

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS , JS
* **Database:** MySQL
* **Tools:** Git, GitHub

---

## 📂 Project Structure

```
shop/
│── manage.py
│── Main/
│   ├── settings.py
│   ├── urls.py
│
│── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│
│── db.sqlite3 / MySQL DB
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-project.git
cd ecommerce-project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django mysqlclient
```

### 4️⃣ Configure Database

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

### 6️⃣ Start Server

```bash
python manage.py runserver
```

---

## 🌐 Usage

* Visit: `http://127.0.0.1:8000/`
* Register a new user
* Login and explore the application

---

## 🔒 Security

* CSRF Protection enabled using Django middleware
* Password fields secured
* Recommended to use environment variables for credentials

---

## 📸 Screenshots

*Add screenshots of your UI here : http://127.0.0.1:8000/Collections/*

---

## 🧠 Future Improvements

* 🛒 Add Cart & Checkout System
* 💳 Payment Gateway Integration
* 📦 Cart
* ⭐ Authentication and Authorization
* 📱 Mobile Optimization

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Sharath M H**

---
