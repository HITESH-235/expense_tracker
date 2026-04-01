# the file handles entrance to the app, managing signups and login
# one of key features is using JWT instead of server remembering user data
# this gives each user a token, shown every time the user accesses data

from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import register_user, authenticate_user

def signup():
    # catch the JSON data from fronted
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password: # checks if both credentials given
        return {"error":"Username and password required"}, 400
    
    # calls the service layer to handle heavy work
    user, error = register_user(username, password)
    if error:
        return {"error":error}, 400
    
    # on success return the user data (returned from service lyaer)
    return {"message":"User added successfully", "user":user.to_dict()}, 201

def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # checks the user if exists from service layer
    user = authenticate_user(username, password)

    if not user: # else user is just None when not found
        return {"error":"Invalid username or password"}, 401
    
    # creates a jwt, with identity of user's id from the column returned (user)
    access_token = create_access_token(identity=str(user.id))

    return {
        "message" : "Login successful",
        "access_token" : access_token,
        "user" : user.to_dict()
    }, 200