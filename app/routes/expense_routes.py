from flask import Blueprint
from app.controllers.expense_controller import *

# Route layer:
# - Define HTTP endpoints.
# - Parse request input.
# - Forward work to controllers.
expense_bp = Blueprint("expenses", __name__)
@expense_bp.route("/expenses",methods=["POST"])
def create_expense():
    return add_expense()


@expense_bp.route("/expenses",methods=["GET"])
def fetch_expenses():
    return get_expenses()


@expense_bp.route("/expense/<int:id>",methods=["GET"])
def fetch_expense(id): # never use the same name as imported func
    return get_expense(id)


@expense_bp.route("/expense/<int:id>",methods=["DELETE"])
def remove_expense(id):
    return delete_expense(id)


@expense_bp.route("/expense/<int:id>", methods=["PUT"])
def edit_expense(id):
    return update_expense(id)


@expense_bp.route("/expenses/total", methods=["GET"])
def total_expense():
    return get_total()


@expense_bp.route("/expenses/summary", methods=["GET"])
def summary():
    return get_summary()


@expense_bp.route("/expenses/summary/monthly", methods=["GET"])
def monthly_expense():
    return get_monthly_summary()


@expense_bp.route("/expenses/summary/weekly", methods=["GET"])
def weekly_expense():
    return get_weekly_summary()