from . import app
from flask import jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

auth = HTTPBasicAuth()
token = HTTPTokenAuth()

@app.route("/health-check", methods=["GET"])
def health_check():
    return jsonify("Healthy")

@app.route("/receipt", methods=["GET"])
@auth.login_required
def receipt():
    return jsonify("generate receipts here")