import os

from dotenv import load_dotenv
from flask import Flask

from app.config import config_by_name
from app.db.database import init_app as init_db
from app.routes.expense_routes import expense_bp


def create_app(config_name: str | None = None) -> Flask:
	load_dotenv()
	app = Flask(__name__)

	config_name = config_name or os.getenv("FLASK_CONFIG", "default")
	app.config.from_object(config_by_name.get(config_name, config_by_name["default"]))

	init_db(app)
	
	# Import models here so Flask-Migrate can detect them
	from app.models import expense_model  # noqa: F401

	app.register_blueprint(expense_bp, url_prefix="/api")

	@app.get("/health")
	def health():  # pragma: no cover - trivial endpoint
		return {"status": "ok"}

	return app
