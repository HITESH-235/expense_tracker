from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.db.database import db
from app.models.expense_model import Expense


class ExpenseSchema(SQLAlchemyAutoSchema):
	class Meta:
		model = Expense
		sqla_session = db.session
		load_instance = True
		include_fk = True

	id = fields.Int(dump_only=True)
	title = fields.Str(required=True, validate=validate.Length(min=1, max=255))
	amount = fields.Decimal(required=True, as_string=True)
	category = fields.Str(allow_none=True, validate=validate.Length(max=100))
	notes = fields.Str(allow_none=True)
	expense_date = fields.Date(required=False)
	created_at = fields.DateTime(dump_only=True)
