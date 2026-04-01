# the file maps all the https methods (GET/POST/...) and url paths

from flask import Blueprint
from app.controllers.expense_controller import *

# blueprint is a mini app, here expense_bp is a mini app for handling all expense urls
expense_bp = Blueprint("expenses", __name__)

# --- CRUD operations ---

@expense_bp.route("/expenses",methods=["POST"])
def create_expense():
    return add_expense() 

@expense_bp.route("/expenses",methods=["GET"])
def fetch_expenses(): # get all expenses list
    return get_expenses()

@expense_bp.route("/expense/<int:id>",methods=["GET"])
def fetch_expense(id): # get expense with given id only
    return get_expense(id)


@expense_bp.route("/expense/<int:id>",methods=["DELETE"])
def remove_expense(id):
    return delete_expense(id)


@expense_bp.route("/expense/<int:id>", methods=["PUT"])
def edit_expense(id): # uses update func, which fetches updates from frontend
    return update_expense(id)


@expense_bp.route("/expenses/total", methods=["GET"])
def total_expense(): # just returns the total amount spent
    return get_total()


@expense_bp.route("/expenses/summary", methods=["GET"])
def summary(): # returns total amount category-wise
    return get_summary()


@expense_bp.route("/expenses/summary/monthly", methods=["GET"])
def monthly_expense(): # each months total amt
    return get_monthly_summary()


@expense_bp.route("/expenses/summary/weekly", methods=["GET"])
def weekly_expense(): # each weeks total amt
    return get_weekly_summary()