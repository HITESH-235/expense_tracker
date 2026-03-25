import os
from flask import Flask
from app.db.database import db
from app.routes.expense_routes import expense_bp
from app.models import expense_model

# def create_app():
# 	print("DB PATH:", os.path.abspath("expenses_db.db"))
# 	app = Flask(__name__)

# 	# uniform resource identifier
# 	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses_db.db" # relative path where db will be created (same folder)
# 	# without this app does not know the db it talks to
# 	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 	# Tracks modifications of objects and sends signals when they change -> turned off

# 	db.init_app(app) # attaches extension(sqalchemy) to flask app
# 	app.register_blueprint(expense_bp, url_prefix="/api")

# 	# makes app aware of its settings, or make db see the uri
# 	with app.app_context():
# 		db.create_all() 
# 		# searches the classes inherited from db.Model
# 		# connexts the location as well
# 		# if file does not exist, runs create table
	
# 	return app

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.getcwd())
    DB_PATH = os.path.join(BASE_DIR, "expenses_db.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(expense_bp)
    from app.models import expense_model

    with app.app_context():
        print("CREATING TABLES...")
        db.create_all()

    return app