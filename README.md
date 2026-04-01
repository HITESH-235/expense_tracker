🪙 Expense Tracker API (v1.0)

A secure, multi-user RESTful API built with Python and Flask. This project handles personal finance tracking with private data isolation, ensuring every user only sees their own financial data.
🚀 Key Features

    User Authentication: Secure Sign-up and Login using JWT (JSON Web Tokens).

    Data Privacy: Strict ownership checks—User A cannot view, edit, or delete User B's expenses.

    Full CRUD: Create, Read, Update, and Delete financial records.

    Smart Analytics: * Total spending calculation.

        Category-based summaries (Food, Rent, etc.).

        Time-based insights (Monthly and Weekly breakdowns).

    Validation Layer: Ensures all incoming data (amounts, dates, categories) is formatted correctly before hitting the database.

🛠️ The Architecture

The project follows a Layered Pattern to keep the code organized and scalable:

    Controllers: The "Bouncers" that handle incoming requests and JWT security.

    Services: The "Managers" that perform the business logic and math.

    Models: The "Blueprints" defining the Database structure (SQLAlchemy).

    Validators: The "Inspectors" ensuring data integrity.

💻 Tech Stack

    Backend: Flask (Python)

    Database: SQLite (SQLAlchemy ORM)

    Security: Flask-JWT-Extended

    Tools: Postman (for API testing)

🚦 Getting Started
1. Installation
Bash

pip install flask flask-sqlalchemy flask-jwt-extended

2. Fire up the Server
Bash

python run.py

3. API Endpoints (Quick Reference)
Method	Endpoint	Description	Auth Required
POST	/auth/register	Create a new account	No
POST	/auth/login	Get your Access Token	No
GET	/expenses	View all your expenses	Yes
POST	/expenses	Log a new expense	Yes
GET	/expenses/total	Get your grand total	Yes
📝 Personal Notes

This project was built to master the flow of data between a client and a server. It emphasizes security and modular code, making it easy to plug in a Frontend (React/Vue) in the future.
How to add this to your project:

    Create a file named README.md in your main folder.

    Paste the text above into it.

    Git Push (one last time with that Token!) to see it rendered beautifully on your GitHub profile.