from typing import List, Optional

from app.db.database import db
from app.models.expense_model import Expense


def list_expenses() -> List[Expense]:
	return Expense.query.order_by(Expense.expense_date.desc()).all()


def get_expense(expense_id: int) -> Optional[Expense]:
	return Expense.query.get(expense_id)


def create_expense(expense: Expense) -> Expense:
	db.session.add(expense)
	db.session.commit()
	return expense


def update_expense(expense: Expense) -> Expense:
	db.session.commit()
	return expense


def delete_expense(expense: Expense) -> None:
	db.session.delete(expense)
	db.session.commit()
