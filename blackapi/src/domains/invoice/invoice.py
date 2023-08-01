import http
import pathlib
import pandas as pd
import uuid
from os import environ
from blackapi.src.repositories.rabbit import Rabbit 
from flask import Blueprint, request, jsonify
from blackapi.src.exceptions.exceptions import FileNotFound, InvalidRequest, PaymentNotProcessed
from uuid import uuid4
from json import dumps
from blackapi.src.utils.logger import logger

bp_invoice = Blueprint("invoice", __name__)

all_fields = ['name', 'governmentId','email','debtAmount','debtDueDate','debtId']

@bp_invoice.route("/invoice/create", methods=["POST"])
def create():
    request_id = str(uuid4())
    logger.info(f'{request_id} | Recived reqquest')
    try:

        if not (request.files and request.files.get('file', None)):
            raise FileNotFound("File not found in this request")

        file = save_file(
                request.files['file'], 
                str(pathlib.Path().absolute()) + "/temp/tempfile-" + str(uuid.uuid1())
            )
            
        if not check_fields(file):
            raise InvalidRequest("Fields not found")
        
        if not process(file):
            raise PaymentNotProcessed("Fail to send message to Rabbit") 

        logger.info(f'{request_id} | Message Processed')
        return jsonify({"status": "processed"}), http.HTTPStatus.OK
            
    except (FileNotFound, InvalidRequest) as error:
        logger.error(f'{request_id} | Invalid Request: {repr(error)}')
        return jsonify({"status": str(error)}), http.HTTPStatus.BAD_REQUEST
    except Exception as error:
        logger.error(f'{request_id} | Unexpected Error: {repr(error)}')
        return jsonify({"status": "Service Unavalible"}), http.HTTPStatus.SERVICE_UNAVAILABLE

def save_file(file, path):
    file.save(path)
    return path

def check_fields(file):
    df = pd.read_csv(file)
    if all([item in df.columns for item in all_fields ]):
        return True
    else:
        return False

def process(file):
    if not environ.get('ENV_TEST'):
        rb = Rabbit()

        content = pd.read_csv(file, names=all_fields, skiprows=[0])
        for i, row in content.iterrows():
            data = build_message(row)
            rb.send_message(queue="invoice", routing_key="invoice", body=dumps(data))

        return True
    
    return True
    
def build_message(row):
    message = {'operation':  'debit'}
    message['name'] = row['name']
    message['governmentId'] = row['governmentId']
    message['email'] = row['email']
    message['debtAmount'] = row['debtAmount']
    message['debtDueDate'] = row['debtDueDate']
    message['debtId'] = row['debtId']
    return message
