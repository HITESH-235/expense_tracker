# Model defines how the expenses are stored
# here a user has one to many relationship, meaning one user can have many expenses

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

# enum class to restrict category values
# this prevents typos in the database
class CategoryEnum(enum.Enum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    RENT = "Rent"
    ENTERTAINMENT = "Entertainment"
    UTILITIES = "Utilities"
    OTHER = "Other"


class Expense(db.Model): # == CREATE TABLE expenses (...);
    __tablename__ = "expenses" # explicitly naming the table in the db

    # defining the Table Columns:
    id = db.Column(db.Integer, primary_key=True) # unique ID for every expense
    amount = db.Column(db.Float, nullable=False) # cost (cant be empty)

    # uses the enum defined above
    category = db.Column(db.Enum(CategoryEnum), nullable=False, default=CategoryEnum.OTHER)

    date = db.Column(db.Date, nullable=False) # stores as a python date object
    description = db.Column(db.String(255), nullable=True)

    # Foreign Key: connects this expense to a specific user's id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # relationship: allows you to access user data from an expense object (e.g., expense.user.username)
    # creates a virtual column 'expenses' in the user model automatically
    user = db.relationship('User', backref = db.backref('expenses', lazy=True)) 

    def to_dict(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "amount" : self.amount,
            
            # extracts the string value from the enum (e.g. "Food")
            "category": self.category.value if hasattr(self.category, 'value') else self.category,
            
            # formats the data object into a "YYYY-MM-DD" form of string (using strftime)
            "date": self.date.strftime('%Y-%m-%d') if self.date else None, # goes like "2026-03-06"
            "description": self.description
        }
    
# convert string to date obj: strptime (string + pattern)
# x = datetime.strptime("2026-03-29", "%Y-%m-%d").date()
# print(x.year + " " + x.month + " " + x.date) => 2026 03 29