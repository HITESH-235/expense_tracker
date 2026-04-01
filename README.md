# 🪙 Expense Tracker API (v1.0)

A secure, multi-user **RESTful API** built with Python and Flask. This project provides a robust backend for personal finance tracking with strict data isolation and JWT-based security.

---

## 🚀 Key Features

* **User Authentication** – Secure Sign-up and Login powered by **JWT** (JSON Web Tokens).
* **Data Privacy** – Strict ownership checks ensure User A can never access User B's records.
* **Full CRUD** – Create, Read, Update, and Delete financial records with ease.
* **Smart Analytics** – 
    * **Total Spending** calculation.
    * **Category Summaries** (e.g., Food, Rent, Entertainment).
    * **Time-based Trends** (Monthly and Weekly breakdowns).
* **Validation Layer** – Automatic checks to ensure amounts, dates, and categories are valid.

---

## 🛠️ The Architecture

The project follows a **Layered Pattern** to maintain clean, scalable code:

> **Controllers:** The "Bouncers" that handle incoming requests and JWT security.  
> **Services:** The "Managers" that perform the core business logic and math.  
> **Models:** The "Blueprints" defining the database structure using SQLAlchemy.  
> **Validators:** The "Inspectors" ensuring data integrity.

---

## 🚦 Getting Started

### 1. Installation
pip install flask flask-sqlalchemy flask-jwt-extended

### 2. Run the Engine
python run.py

### 3. Core Endpoints
| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/register` | Create a new account | No |
| `POST` | `/auth/login` | Get your Access Token | No |
| `GET` | `/expenses` | View all your expenses | **Yes** |
| `POST` | `/expenses` | Log a new expense | **Yes** |
| `GET` | `/expenses/total` | Get your grand total | **Yes** |
| `GET` | `/expenses/summary` | Category breakdown | **Yes** |
| `GET` | `/expenses/monthly` | Monthly trends | **Yes** |

---

## 💻 Tech Stack
* **Backend:** Flask (Python)
* **Database:** SQLite (SQLAlchemy ORM)
* **Security:** Flask-JWT-Extended
* **Testing:** Postman

---

## 📝 Final Notes
Built with a focus on **security** and **modular architecture**. This backend is designed to be easily integrated with any modern Frontend framework (React, Vue, etc.).