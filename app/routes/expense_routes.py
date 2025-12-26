from flask import Blueprint, request

from app.controllers import expense_controller

expense_bp = Blueprint("expenses", __name__)


@expense_bp.get("/expenses")
def list_expenses():
	return expense_controller.list_expenses()


@expense_bp.get("/expenses/<int:expense_id>")
def get_expense(expense_id: int):
	return expense_controller.get_expense(expense_id)


@expense_bp.post("/expenses")
def create_expense():
	payload = request.get_json(force=True, silent=False) or {}
	return expense_controller.create_expense(payload)


@expense_bp.put("/expenses/<int:expense_id>")
def update_expense(expense_id: int):
	payload = request.get_json(force=True, silent=False) or {}
	return expense_controller.update_expense(expense_id, payload)


@expense_bp.delete("/expenses/<int:expense_id>")
def delete_expense(expense_id: int):
	return expense_controller.delete_expense(expense_id)
