# the file acts as the manager for all expenses data
# performs calcs, handles complex filtering, 
# and ensures data from internet is converted into a format the database understands

from app.models.expense_model import Expense, CategoryEnum
from app.db.database import db
from sqlalchemy import func, extract
from datetime import datetime


def create_expense(data, user_id):
    # converts the string(date) into a python date object
    date_obj = datetime.strptime(data["date"], "%Y-%m-%d").date()

    expense = Expense(
        amount = data["amount"],
        # converts the string category (e.g. "Food") into its enum type
        category=CategoryEnum[data.get('category').upper()],
        date = date_obj,
        description = data.get("description"), # .get() handles missing description
        user_id = user_id
    )
    db.session.add(expense)
    db.session.commit()
    return expense


def get_all_expenses(filters, user_id):
    query = Expense.query.filter_by(user_id=user_id)

    # --- Filtering Logic ---
    # dynamically adds "WHERE" clauses to the sql query data based on the user input
    if "category" in filters:
        query = query.filter_by(category=CategoryEnum(filters["category"]))
    if "min_amount" in filters:
        query = query.filter(Expense.amount >= float(filters["min_amount"]))
    if "max_amount" in filters:
        query = query.filter(Expense.amount <= float(filters["max_amount"]))

    # --- Sorting Logic ---
    sort = filters.get("sort") # since we didnt check if sort attrib exists
    if sort == "amount_asc":
        query = query.order_by(Expense.amount.asc())
    elif sort == "amount_desc":
        query = query.order_by(Expense.amount.desc())

    if sort == "date_asc":
        query = query.order_by(Expense.date.asc())
    if sort == "date_desc":
        query = query.order_by(Expense.date.desc())

    return query.all() # execute the final built query


def get_expense_by_id(id): # returns the expense if exists else none
    return Expense.query.get(id)


def delete_expense_by_id(id):
    expense = Expense.query.get(id)
    if not expense: return None # cant delete if not existing, return falsy

    db.session.delete(expense)
    db.session.commit()
    return True


def update_expense_by_id(id, data): # check for each col(arg) explicitly
    expense = Expense.query.get(id)

    if not expense: return None
    # only update fields that are actually provided in the request
    if "amount" in data: expense.amount = float(data["amount"])
    if "category" in data: expense.category = CategoryEnum(data["category"])
    if "date" in data: 
        expense.date = datetime.strptime(data["date"], "%Y-%m-%d").date()
    if "description" in data:
        expense.description = data["description"]

    db.session.commit()
    return expense


# --- Analytics Functions ---
# uses sql aggregate funcs to do math at the server side

def get_total_expense():
    # .scalar() returns the single numeric result of the sum
    total = db.session.query(func.sum(Expense.amount)).scalar()
    return total or 0


def get_category_summary():
    # here group_by will allow to see totals for each category like Food, Rent.. 
    res = db.session.query(
        Expense.category, 
        func.sum(Expense.amount)
    ).group_by(Expense.category).all()
    # returns a dict for the frontend
    return {category.value:amount for category, amount in res}


# monthly expense chart
def get_monthly_expense_summary():
    # extracts specific parts (year/month) out of a date column
    res = db.session.query(
        extract('year', Expense.date).label('year'), # first element
        extract('month', Expense.date).label('month'), # second
        func.sum(Expense.amount) # third
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