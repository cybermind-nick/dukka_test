import os
from flask import Blueprint, jsonify, request, request_started
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from .models import User, db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required

user = Blueprint("user", __name__, url_prefix="/user")

auth = HTTPBasicAuth()

@user.get("/")
def index():
    return jsonify("User endpoints")

@user.post("/register")
def register():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]

    if User.query.filter_by(email=email).first() is not None:
        jsonify({"error": "email already exists"}), 409
    
    if User.query.filter_by(username=username).first() is not None:
        jsonify({"error": "username already exists"}), 409

    if len(password) < 6:
        jsonify({"error": "password too short"}), 400

    if len(username) < 3:
        jsonify({"error": "username too short"}), 400
    
    if not username.isalnum():
        jsonify({"error": "username should be alphanumeric"}), 400
    
    if not validators.email(email):
        jsonify({"error": "email not valid"}), 400

    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "user created",
        "User": {
            "username": username,
            "email": email
        }
    }), 201

@user.post('/login')
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': user.username,
                    'email': email
                }
            }), 200
    
    return jsonify({
        'error': 'Wring credentials'
    }), 401

# @user.route("/purchase", endpoint='purchase', methods=['POST'])
# @jwt_required
# def purchase():

#     return jsonify("purchase")

@user.get('/receipt')
@jwt_required
def receipt():
    pass
