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
    update_expense_by_id
)

def add_expense():
    data = request.get_json()
    
    # none if no errors, else holds error message
    error = validate_expense_data(data)
    if (error): return {"error":error}, 400
    
    expense = create_expense(data)
    return expense.to_dict(), 201


def get_expenses():
    expenses = get_all_expenses()
    return [e.to_dict() for e in expenses], 200


def get_expense(id):
    expense = get_expense_by_id(id) # returns none if not found

    if not expense: return {"error":"Expense not found"}, 404
    
    return expense.to_dict(), 200


def delete_expense(id):
    res = delete_expense_by_id(id) # returns none if not found

    if not res: return {"error":"Expense not found"}, 404
        
    return {"message":"Expense deleted"}, 200


def update_expense(id):
    data = request.get_json()

    error = validate_expense_data(data, partial=True)
    if error: return {"error":error}, 400
    
    expense = update_expense_by_id(id, data)
    if not expense: return {"error":"Expense not found"}, 404
    
    return expense, 200