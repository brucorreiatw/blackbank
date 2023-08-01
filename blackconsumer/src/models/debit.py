from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.utils.logger import logger

class Debit:
    def __init__(self) -> None:
        pass

    def debit_proccess(self):
        ...

    def _insert_database(self):
        ...

    def _create_boleto(self):
        ...

    def _send_email(self):
        ...