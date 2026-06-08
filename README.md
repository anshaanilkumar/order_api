# Order Management API

A simple Order Management API built using Django and Django REST Framework with JWT authentication and role-based access control.

---

## 🚀 Features

* User Registration (Admin & Customer)
* JWT Authentication (Login)
* Role-Based Access Control
* Product Management (Admin only)
* Order Creation with Nested Items
* Order Total Calculation
* Customers can view only their orders
* Admin can view and update all orders

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/anshaanilkumar/order_api.git
cd order_api/config
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install django djangorestframework djangorestframework-simplejwt
```

4. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Run server:

```
python manage.py runserver
```

---

## 🔐 Authentication

Uses JWT Token

```

## 📦 API Endpoints

### 1. Register

```
POST /api/register/
```

### 2. Login

```
POST /api/login/
```

### 3. Products

* GET `/api/products/`
* POST `/api/products/create/` (Admin only)

### 4. Orders

* GET `/api/orders/`
* POST `/api/orders/create/`
* PUT `/api/orders/update/<id>/` (Admin only)

---

## 🛒 Sample Order Request

```
{
  "items": [
    {"product": 1, "quantity": 2},
    {"product": 2, "quantity": 1}
  ]
}
```

---

## 🎯 Role Permissions

| Role     | Permissions                  |
| -------- | ---------------------------- |
| Admin    | Manage products & all orders |
| Customer | Create & view own orders     |


