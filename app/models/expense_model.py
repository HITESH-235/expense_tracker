import enum
from app.db.database import db

# CREATE TABLE expenses (
#     id INTEGER PRIMARY KEY,
#     amount FLOAT NOT NULL,
#     category VARCHAR(50) NOT NULL,
#     date VARCHAR(20) NOT NULL
# );

# the Expense class inherits from the db.Model class, 
# which already has a constructor that accepts keyword args, not ordered args
# the primary key isnt given as argument, can create conflicts, automatically handled
# e.g. x = Expense(amount=500, category="food", date="05-03-2026") 


class CategoryEnum(enum.Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    RENT = "Rent"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"


class Expense(db.Model): # == CREATE TABLE expenses (...);
    __tablename__ = "expenses" # sets actual db table name

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False) # cant be empty

    # only allow values that exist inside the CategoryEnum class
    category = db.Column(db.Enum(CategoryEnum), nullable=False, default=CategoryEnum.OTHER)

    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "id" : self.id,
            "amount" : self.amount,
            "category": self.category.value if hasattr(self.category, 'value') else self.category,
            # converting date obj back to a string for JSON(frontend) using strftime (date to str)
            "date": self.date.strftime('%Y-%m-%d') if self.date else None, # goes like "2026-03-06"
            "description": self.description
        }
    
# convert string to date obj: strptime (string + pattern)
# x = datetime.strptime("2026-03-29", "%Y-%m-%d").date()
# print(x.year + " " + x.month + " " + x.date) => 2026 03 29