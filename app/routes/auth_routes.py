from flask import Blueprint
from app.controllers.auth_controller import signup, login

# new blueprint for handling signup/signin by user
auth_bp = Blueprint('auth_bp', __name__)
                                
auth_bp.route('/register', methods=['POST'])(signup)
auth_bp.route('/login', methods=['POST'])(login)