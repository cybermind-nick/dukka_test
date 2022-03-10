from . import app
from flask import jsonify


@app.route("/health-check", methods=["GET"])
def health_check():
    return jsonify("Healthy")
