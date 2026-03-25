"""Model layer.

Responsibility:
- Define SQLAlchemy models and table structure.

TODO:
- Add Expense model fields and metadata.
"""

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

class Expense(db.Model): # == CREATE TABLE expenses (...);
    __tablename__ = "expenses" # sets actual db table name

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False) # cant be empty
    category = db.Column(db.String(50), nullable=False) # max length 50 allowed
    date = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "amount" : self.amount,
            "category": self.category,
            "date": self.date
        }