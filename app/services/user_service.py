# this file handles the security and gatekeeping of app, managing user creation and verification
# never interacts with the app directly, only talks to the hashing logic in the user_model

from app.models.user_model import User
from app.db.database import db


def register_user(username, password):
    # validation: check if the name is already not already taken
    if User.query.filter_by(username=username).first(): # checks if user already exists
        return None, "Username already exists"
    
    new_user = User(username=username)
    # triggers the hashing logic, written in the user_model:
    new_user.set_password(password) # set password but in hashed form

    db.session.add(new_user)
    db.session.commit()
    return new_user, None


def authenticate_user(username, password):
    # find the user by name
    user = User.query.filter_by(username=username).first()
    # if usee exists, this asks the model to check if the password matches the password_hashed
    if user and user.check_password(password):
        return user
    return None # for invalid credentials
