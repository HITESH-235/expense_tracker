import os
from flask import Flask
from app.db.database import db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.getcwd())
    DB_PATH = os.path.join(BASE_DIR, "expenses_db.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = 'dev-secret-47'

    jwt = JWTManager(app)

    db.init_app(app) # connects sqlalch. database into specific flask app

    from app.routes.expense_routes import expense_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(expense_bp) # plugs in the set of routes into app
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.models import expense_model, user_model

    with app.app_context(): # give db temp. permission to look at app settings and build tables
        print("CREATING TABLES...")
        db.create_all()

    return app