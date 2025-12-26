from flask import abort

from app.schemas.expense_schema import ExpenseSchema
from app.services import expense_service
from app.db.database import db

expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)


def list_expenses():
	expenses = expense_service.list_expenses()
	return expenses_schema.dump(expenses), 200


def get_expense(expense_id: int):
	expense = expense_service.get_expense(expense_id)
	if not expense:
		abort(404, description="Expense not found")
	return expense_schema.dump(expense), 200


def create_expense(payload: dict):
	expense = expense_schema.load(payload)
	created = expense_service.create_expense(expense)
	return expense_schema.dump(created), 201


def update_expense(expense_id: int, payload: dict):
	expense = expense_service.get_expense(expense_id)
	if not expense:
		abort(404, description="Expense not found")
	expense_schema.load(payload, instance=expense, session=db.session, partial=True)
	updated = expense_service.update_expense(expense)
	return expense_schema.dump(updated), 200


def delete_expense(expense_id: int):
	expense = expense_service.get_expense(expense_id)
	if not expense:
		abort(404, description="Expense not found")
	expense_service.delete_expense(expense)
	return {}, 204
