from sqlalchemy import Column, Float, Integer, String

from src.models import base


class Credit(base):
    __tablename__ = 'Credits'
    debtId = Column(String(100), primary_key=True)
    paidAt = Column(String(100))
    paidAmount = Column(String(100))
    paidBy = Column(String(100))

    def __init__(self, msg):
        self.debtId = msg['debtId']
        self.paidAt = msg['paidAt']
        self.paidAmount = msg['paidAmount']
        self.paidBy = msg['paidBy']

    def execute(self):
        # ver se tem debit
        # caso positivo remov eo débito
        pass