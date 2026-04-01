# the file connects the validator with service layer, ensuring every response sent is checked, with status

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
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

@jwt_required()
def add_expense():
    # silent prevents an instant 400 crash without err msg if the request is empty
    data = request.get_json(silent=True)

    if data is None: return {"error":"Request body must be JSON"}, 400
    
    # uses validation layer to check if all attributes given are valid
    error = validate_expense_data(data)
    if (error): return {"error":error}, 400

    current_user_id = get_jwt_identity() # Grabs '47' from your token
    expense = create_expense(data, current_user_id)
    
    return expense.to_dict(), 201

@jwt_required()
def get_expenses():
    filters = request.args.to_dict() # collects any extra arg given like category/sort from request
    current_user_id = get_jwt_identity() # Get the ID
    expenses = get_all_expenses(filters, current_user_id)

    # return as list but with each element as dictionary
    return [e.to_dict() for e in expenses], 200

@jwt_required()
def get_expense(id):
    current_user_id = get_jwt_identity() # Get the ID
    expense = get_expense_by_id(id, current_user_id)
    if not expense: return {"error":"Expense not found"}, 404
    
    return expense.to_dict(), 200

@jwt_required()
def delete_expense(id): 
    current_user_id = get_jwt_identity() # Get the ID
    res = delete_expense_by_id(id, current_user_id) # returns none if not found

    if not res: return {"error":"Expense not found"}, 404

    # 204 is when action is successful, but no msg is req in response (like for deletion)
    return "", 204

@jwt_required()
def update_expense(id):
    data = request.get_json(silent=True)

    if data is None: return {"error":"Request body must be JSON"}, 400

    # partial = True allows user to update only amt
    error = validate_expense_data(data, partial=True) # if cant update returns err msg
    if error: return {"error":error}, 400

    current_user_id = get_jwt_identity() # Get the ID
    expense = update_expense_by_id(id, data, current_user_id)
    if not expense: return {"error":"Expense not found"}, 404
    return expense.to_dict(), 200


# --- Analytics Controllers ---
# simply fetches the calculated data from the service layer and return it in json

@jwt_required()
def get_total():
    current_user_id = get_jwt_identity()
    total = get_total_expense(current_user_id)
    return {"total":total}, 200

@jwt_required()
def get_summary():
    current_user_id = get_jwt_identity()
    summary = get_category_summary(current_user_id)
    return summary, 200

@jwt_required()
def get_monthly_summary():
    current_user_id = get_jwt_identity() 
    data = get_monthly_expense_summary(current_user_id) 
    return data, 200

@jwt_required() 
def get_weekly_summary():
    current_user_id = get_jwt_identity() 
    data = get_weekly_expense_summary(current_user_id) 
    return data, 200