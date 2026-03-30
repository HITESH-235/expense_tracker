from app.models.expense_model import Expense
from app.db.database import db
from sqlalchemy import func, extract
from datetime import datetime


def create_expense(data): # errors already addressed in controller
    date_obj = datetime.strptime(data["date"], "%Y-%m-%d").date()

    expense = Expense( # or just do Expense(**data)
        amount = data["amount"],
        category = data["category"],
        date = date_obj
    )
    db.session.add(expense)
    db.session.commit()
    return expense


def get_all_expenses(filters): # no error can be created for this task
    query = Expense.query

    # --- filtering ---
    if "category" in filters:
        query = query.filter_by(category=filters["category"])
    if "min_amount" in filters:
        query = query.filter(Expense.amount >= float(filters["min_amount"]))
    if "max_amount" in filters:
        query = query.filter(Expense.amount <= float(filters["max_amount"]))

    # --- sorting ---
    sort = filters.get("sort") # since we didnt check if sort attrib exists
    if sort == "amount_asc":
        query = query.order_by(Expense.amount.asc())
    elif sort == "amount_desc":
        query = query.order_by(Expense.amount.desc())

    if sort == "date_asc":
        query = query.order_by(Expense.date.asc())
    if sort == "date_desc":
        query = query.order_by(Expense.date.desc())

    return query.all() # no query, no filtering


def get_expense_by_id(id): # the get statement itself returns None
    return Expense.query.get(id)


# important to handle errors in functions that change database
def delete_expense_by_id(id):
    expense = Expense.query.get(id)
    if not expense: return None

    db.session.delete(expense)
    db.session.commit()
    return True


def update_expense_by_id(id, data): # check for each col(arg) explicitly
    expense = Expense.query.get(id)

    if not expense: return None
    if "amount" in data: expense.amount = float(data["amount"])
    if "category" in data: expense.category = data["category"]
    if "date" in data: 
        expense.date = datetime.strptime(data["date"], "%Y-%m-%d").date()

    db.session.commit()
    return expense


def get_total_expense():
    total = db.session.query(func.sum(Expense.amount)).scalar()
    return total or 0


def get_category_summary():
    res = db.session.query(
        Expense.category, 
        func.sum(Expense.amount)
    ).group_by(Expense.category).all()
    return {category:amount for category, amount in res}


# monthly expense chart
def get_monthly_expense_summary():
    res = db.session.query(
        extract('year', Expense.date).label('year'),
        extract('month', Expense.date).label('month'),
        func.sum(Expense.amount)
    ).group_by('year', 'month').order_by('year', 'month').all()

    return [{
        'year': int(year),
        'month': int(month),
        'total': total
    } for year, month, total in res ]


def get_weekly_expense_summary():
    res = db.session.query(
        extract('year', Expense.date).label('year'),
        extract('week', Expense.date).label('week'),
        func.sum(Expense.amount)
    ).group_by('year', 'week').order_by('year', 'week').all()

    return [
        {
            'year': int(year),
            'week': int(week),
            'total': total
        } for year,week, total in res
    ]