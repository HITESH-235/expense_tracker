# this file defines the structure of the users table in database
# also handles security by hashing passwords

from app.db.database import db
# werkzeug is a utility library that flask uses for security
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False) # no two users can have the same name
    password_hash = db.Column(db.String(255), nullable=False) # scrambled version of the product

    def set_password(self, password):
        # hashes teh plain password provided and stores to the DB
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # compares a provided password with the stored hash
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        # returns non sensitive user data for the api responses, hence no password included
        return {
            "id" : self.id,
            "username" : self.username
        }