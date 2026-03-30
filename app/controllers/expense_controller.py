"""Controller layer.

Responsibility:
- Receive validated request data from routes.
- Coordinate service calls.
- Return API responses.

TODO:
- Add expense CRUD controller functions.
"""

from flask import request
from app.utils.validators import validate_expense_data
from app.services.expense_service import (
    create_expense, 
    get_all_expenses, 
    get_expense_by_id, 
    delete_expense_by_id, 
    update_expense_by_id,
    get_total_expense,
    get_category_summary,
    get_monthly_expense_summary,
    get_weekly_expense_summary,
)

def add_expense():
    data = request.get_json(silent=True) # silent keyword stops crashing when no json

    if data is None: return {"error":"Request body must be JSON"}, 400
    
    # none if no errors, else holds error message
    error = validate_expense_data(data)
    if (error): return {"error":error}, 400
    
    expense = create_expense(data)
    return expense.to_dict(), 201


def get_expenses():
    filters = request.args.to_dict()
    expenses = get_all_expenses(filters)
    return [e.to_dict() for e in expenses], 200


def get_expense(id):
    expense = get_expense_by_id(id) # returns none if not found

    if not expense: return {"error":"Expense not found"}, 404
    
    return expense.to_dict(), 200


def delete_expense(id):
    res = delete_expense_by_id(id) # returns none if not found

    if not res: return {"error":"Expense not found"}, 404
        
    return "", 204 # code for no content return (yet successful) 


def update_expense(id):
    data = request.get_json(silent=True)

    if data is None: return {"error":"Request body must be JSON"}, 400

    error = validate_expense_data(data, partial=True)
    if error: return {"error":error}, 400

    expense = update_expense_by_id(id, data)
    if not expense: return {"error":"Expense not found"}, 404

    return expense.to_dict(), 200


def get_total():
    total = get_total_expense()
    return {"total":total}, 200


def get_summary():
    summary = get_category_summary()
    return summary, 200


def get_monthly_summary():
    data = get_monthly_expense_summary()
    return data, 200


def get_weekly_summary():
    data = get_weekly_expense_summary()
    return data, 200