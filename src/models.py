# Create the db model and...
# ...define the entites on the pdf receipt
# Structure out the pdf

from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import os
import base64


basedir = os.path.abspath(os.path.dirname(__file__))

db_filename = 'database.db'
db_path = "sqlite:///{}".format(os.path.join(basedir, db_filename))
db = SQLAlchemy()

# print(db_path)

def db_setup(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create():
    db.drop_all()
    db.create_all()

# defining models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    purchase = db.relationship('Purchase', backref="user")

    # token = db.Column(db.String(32), unique=True, index=True)
    # token_expiration = db.Column(db.DateTime)

    # def get_token(self, expires_in=3600):
    #     now = datetime.utcnow()
    #     if self.token and self.token_expiration > now + timedelta(seconds=60):
    #         return self.token
    #     self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
    #     self.token_expiration = now + timedelta(seconds=expires_in)
    #     db.session.add(self)
    #     return self.token

    # def revoke_token(self):
    #     self.token_expiration = datetime.utcnow() - timedelta(seconds=600)
    
    # @staticmethod
    # def check_token(token):
    #     user = User.query.filter_by(token=token).first()
    #     if user is None or user.token_expiration < datetime.utcnow():
    #         return None
    #     return user
    

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column()
    item = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    purchased_at = db.Column(db.DateTime, default=datetime.now())

# class Item(db.Model):
#     item_id = db.Column(db.Integer)