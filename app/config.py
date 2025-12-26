import os
from urllib.parse import quote_plus


class Config:
	"""Base configuration loaded from environment variables."""

	SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
	SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or (
		"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
			user=quote_plus(os.getenv("MYSQL_USER", "expense_user")),
			password=quote_plus(os.getenv("MYSQL_PASSWORD", "expense_pass")),
			host=os.getenv("MYSQL_HOST", "localhost"),
			port=os.getenv("MYSQL_PORT", "3306"),
			database=os.getenv("MYSQL_DATABASE", "expense_tracker"),
		)
	)
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
	TESTING = True


config_by_name = {
	"default": Config,
	"testing": TestingConfig,
}
