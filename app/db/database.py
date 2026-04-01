# this file is the conductor bw the python code and the database engine (sqlite)
# while sqlalchemy is a python sql toolkit and object relational mapper (ORM, maps python classes to database tables)

from flask_sqlalchemy import SQLAlchemy

# initialises the sqlalchemy object
db = SQLAlchemy() # this obj will be used throughout the app to interact with the database