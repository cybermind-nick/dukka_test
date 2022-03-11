# Create the db model and...
# ...define the entites on the pdf receipt
# Structure out the pdf

from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

db_filename = 'database.db'
db_path = "sqlite:///{}".format(os.path.join(basedir, db_filename))
db = SQLAlchemy()


# sqlite database configuration
def db_setup(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create():
    db.create_all()

# defining models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True, index=True)
    password = db.Column(db.Text(), nullable=False)
    phone = db.Column(db.Integer, nullable = False, unique=True)
    purchase = db.relationship('Purchase', backref="user")


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    purchased_at = db.Column(db.DateTime, default=datetime.now())
    amount = db.Column(db.Integer, nullable=False)