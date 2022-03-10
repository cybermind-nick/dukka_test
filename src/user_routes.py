from datetime import datetime
import os
from flask import Blueprint, jsonify, request, send_file
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from .models import Purchase, User, db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flasgger import swag_from
from src.receipt import generate_receipt

user = Blueprint("user", __name__, url_prefix="/user")

@user.get("/")
def index():
    return jsonify("User endpoints")

@user.post("/register")
@swag_from('./docs/user/register.yml')
def register():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    phone = request.json["phone"]
    address = request.json["address"]

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "email already exists"}), 409
    
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"error": "username already exists"}), 409

    if len(password) < 6:
        return jsonify({"error": "password too short"}), 400

    if len(username) < 3:
        return jsonify({"error": "username too short"}), 400
    
    if not username.isalnum():
        return jsonify({"error": "username should be alphanumeric"}), 400
    
    if not validators.email(email):
        return jsonify({"error": "email not valid"}), 400

    pwd_hash = generate_password_hash(password)

    user = User(username=username, password=pwd_hash, email=email, address=address, phone=phone)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "user created",
        "User": {
            "username": username,
            "email": email,
            "phone": phone,
            "address": address
        }
    }), 201

@user.post('/login')
@swag_from('./docs/user/login.yml')
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


# item purchase
@user.post('/purchase')
@jwt_required()
@swag_from('./docs/user/purchase.yml')
def purchase():

    item = request.json.get('item')
    amount = request.json.get('amount')

    user_id = get_jwt_identity()

    user = User.query.filter_by(id=user_id).first()

    purchase = Purchase(item=item, user_id=user_id, amount=amount)
    db.session.add(purchase)
    db.session.commit()

    return jsonify({
        "purchase by": user.username,
        "item": item,
        "amount": amount,
        }), 200


# generate receipt for user
@user.get('/receipt')
@jwt_required()
@swag_from('./docs/user/receipt.yml')
def receipt():

    user_id = get_jwt_identity()

    purchase = Purchase.query.filter_by(user_id=user_id).first()

    if purchase:

        user = User.query.filter_by(id=user_id).first()


        generate_receipt(
            item=purchase.item, amount=purchase.amount,
            name= user.username, phone=user.phone, address=user.address,
            email=user.email, date=datetime.now().date()
            )

        return jsonify({
            "item": purchase.item,
            "amount": purchase.amount,
            "message": "receipt generated and saved"
        }), 200

    else:
        return jsonify({
            "error": "No purchase on account, cannot generate receipt"
        }), 403

@user.get('/receipt/download')
@jwt_required()
@swag_from('./docs/user/receipt_download.yml')
def download():
    user_id = get_jwt_identity()

    user = User.query.filter_by(id=user_id).first()

    if os.path.exists(f'../receipts/{user.phone}.pdf'):
        return send_file(f'../receipts/{user.phone}.pdf', as_attachment=True)
    
    else:
        return jsonify({
            "error": "Receipt not found"
        }), 404
