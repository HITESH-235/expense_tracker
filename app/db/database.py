from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
	"""Initialize extensions with the Flask app."""
	db.init_app(app)
	migrate.init_app(app, db)
