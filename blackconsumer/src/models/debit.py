from sqlalchemy import Column, Float, Integer, String

from src.models import base
from src.repositories.postgresql import postgsql


class Debit(base):
    __tablename__ = 'Debits'
    debtId = Column(String(100), primary_key=True)
    name = Column(String(100))
    governmentId = Column(String(100))
    email = Column(String(100))
    debtAmount = Column(String(100))
    debtDueDate = Column(String(100))

    def __init__(self, msg):
        self.debtId = msg['debtId']
        self.name = msg['name']
        self.governmentId = msg['governmentId']
        self.email = msg['email']
        self.debtAmount = msg['debtAmount']
        self.debtDueDate = msg['debtDueDate']

    def execute(self):
        postgsql.insert(self)

    def _insert_database(self):
        ...

    def _create_boleto(self):
        ...

    def _send_email(self):
        ...