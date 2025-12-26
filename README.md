# Expense Tracker

A Flask-based REST API for tracking expenses with MySQL database.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   - Copy `.env` and update MySQL credentials
   - Or set `DATABASE_URL` directly

3. **Setup MySQL database:**
   ```bash
   # Create database and user
   mysql -u root -p
   CREATE DATABASE expense_tracker;
   CREATE USER 'expense_user'@'localhost' IDENTIFIED BY 'expense_pass';
   GRANT ALL PRIVILEGES ON expense_tracker.* TO 'expense_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. **Initialize database migrations:**
   ```bash
   export FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   python run.py
   # Or: flask run
   ```

## API Endpoints

Base URL: `http://localhost:5000/api`

- `GET /expenses` - List all expenses
- `GET /expenses/<id>` - Get single expense
- `POST /expenses` - Create new expense
- `PUT /expenses/<id>` - Update expense
- `DELETE /expenses/<id>` - Delete expense
- `GET /health` - Health check

## Example Request

```bash
curl -X POST http://localhost:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Lunch",
    "amount": "12.50",
    "category": "Food",
    "expense_date": "2025-12-26"
  }'
```

## Project Structure

```
app/
├── __init__.py          # App factory
├── config.py            # Configuration
├── controllers/         # Request handlers
├── db/                  # Database initialization
├── models/              # SQLAlchemy models
├── routes/              # API blueprints
├── schemas/             # Marshmallow schemas
└── services/            # Business logic
```
