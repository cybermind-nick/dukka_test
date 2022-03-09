'''
    Authentication and authorisation middleware
'''

from flask_httpauth import HTTPBasicAuth

from models import User

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()

