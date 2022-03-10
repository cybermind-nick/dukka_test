from crypt import methods
import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .user_routes import *
from .models import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config

def create_app():
    app = Flask(__name__)

    CORS(app)

    JWTManager(app)

    Swagger(app, config=swagger_config, template=template)



    print(db_filename)

    db_setup(app)
    db_drop_and_create()
    app.register_blueprint(user)

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['SWAGGER'] = {
        'title': "Dukka Backend Test",
        'uiversion': 3
    }

    # app.add_url_rule('/user', view_func=Main.as_view('user'), methods=['GET'])

    return app



app = create_app()

from .routes import *