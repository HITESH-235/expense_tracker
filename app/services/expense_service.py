from app.models.expense_model import Expense
from app.db.database import db

def create_expense(data): # errors already addressed in controller
    expense = Expense( # or just do Expense(**data)
        amount = data["amount"],
        category = data["category"],
        date = data["date"]
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

    # if sort == "date_asc": # since date is string, this does not work as intende
    #     query = query.order_by(Expense.date.asc())
    # if sort == "date_asc":
    #     query = query.order_by(Expense.date.desc())

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
    if "date" in data: expense.date = data["date"]

    db.session.commit()
    return expense