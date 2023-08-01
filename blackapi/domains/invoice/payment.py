import http
from blackapi.repositories.rabbit import Rabbit 
from flask import Blueprint, request, jsonify
from os import environ
from json import dumps
from uuid import uuid4
from blackapi.exceptions.exceptions import InvalidRequest, PaymentNotProcessed
from blackapi.utils.logger import logger

bp_payment = Blueprint("payment", __name__)

@bp_payment.route("/payment/create", methods=["POST"])
def create():
    request_id = str(uuid4())
    logger.info(f'{request_id} | Received reqquest')
    try:
        payload = request.json
        if not validate_request(payload):
            raise InvalidRequest("Incomplete Payload")
        
        if not process(request.json):
            raise PaymentNotProcessed("Fail to send message to Rabbit")

        logger.info(f'{request_id} | Message Processed')
        return jsonify({"status": "processed"}), http.HTTPStatus.OK
        
    except InvalidRequest as error:
        logger.error(f'{request_id} | Bad Request: {repr(error)}')
        return jsonify({"status": str(error)}), http.HTTPStatus.BAD_REQUEST
    except Exception as error:
        logger.error(f'{request_id} | Unexpected Error: {repr(error)}')
        return jsonify({"status": "Service Unavalible"}), http.HTTPStatus.SERVICE_UNAVAILABLE


def validate_request(payload):
    all_fields = ['debtId', 'paidAt', 'paidAmount', 'paidBy']
    for field in all_fields:
        if not field in payload:
            return False

    return True

def process(data):
    if not environ.get('ENV_TEST'):
        rb = Rabbit()

        data["operation"] = "credit"

        rb.send_message(queue="invoice", routing_key="invoice", body=dumps(data))
        
        return True
    return True