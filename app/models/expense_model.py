from datetime import datetime, date

from app.db.database import db


class Expense(db.Model):
	__tablename__ = "expenses"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	amount = db.Column(db.Numeric(10, 2), nullable=False)
	category = db.Column(db.String(100), nullable=True)
	notes = db.Column(db.Text, nullable=True)
	expense_date = db.Column(db.Date, nullable=False, default=date.today)
	created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

	def __repr__(self) -> str:  # pragma: no cover - debug helper
		return f"<Expense {self.id} {self.title} {self.amount}>"
