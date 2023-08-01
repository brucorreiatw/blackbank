import http
from flask import Blueprint, jsonify

bp_healthcheck = Blueprint("healthcheck", __name__)

@bp_healthcheck.route("/liveness", methods=["GET"])
def liveness():
    try:
        return jsonify({"status": "green"}), http.HTTPStatus.OK
    except:
        return jsonify({"status": "red"}), 500

@bp_healthcheck.route("/readiness", methods=["GET"])
def readiness():
    try:
        return jsonify({"status": "green"}), http.HTTPStatus.OK
    except:
        return jsonify({"status": "red"}), 500