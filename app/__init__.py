import os
from flask import Flask
from app.db.database import db
from flask_jwt_extended import JWTManager
from datetime import timedelta

def create_app():
    app = Flask(__name__)

    # --- database configuration ---
    # find the absolute path of project, so db file stays at right place
    BASE_DIR = os.path.abspath(os.getcwd())
    DB_PATH = os.path.join(BASE_DIR, "expenses_db.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # saves memory to put this off

    # --- security(jwt) configuration ---
    app.config["JWT_SECRET_KEY"] = 'dev-secret-47'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

    jwt = JWTManager(app) # initiate the jwt manager

    db.init_app(app) # connects sqlalch. database into specific flask app

    # --- blueprints ---
    # imported inside to prevent "circular imports"
    # (the routes need app, before its even created)
    from app.routes.expense_routes import expense_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(expense_bp) # plugs in the set of routes into app
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # import models so sqlalchemy knows which tables to build
    from app.models import expense_model, user_model

    with app.app_context(): # sets the current_app=app so db can access config (settings)
        print("CREATING TABLES...") # use this app's database to store tables
        db.create_all()

    return app