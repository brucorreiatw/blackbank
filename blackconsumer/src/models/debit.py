from sqlalchemy import Column, Float, Integer, String, Date

from src.models import base
from src.repositories.postgresql import postgsql
from src.utils.logger import logger
from uuid import uuid4


class Debit(base):
    __tablename__ = 'Debits'
    debtId = Column(Integer, primary_key=True)
    name = Column(String(100))
    governmentId = Column(String(100))
    email = Column(String(100))
    debtAmount = Column(Float)
    debtDueDate = Column(Date)

    def __init__(self, msg):
        self.debtId = msg['debtId']
        self.name = msg['name']
        self.governmentId = msg['governmentId']
        self.email = msg['email']
        self.debtAmount = msg['debtAmount']
        self.debtDueDate = msg['debtDueDate']

    def execute(self):
        postgsql.insert(self)
        boleto = self._create_boleto(self.debtId, self.governmentId, self.debtAmount, self.debtAmount)
        self._send_email(self.name, self.email, boleto)

    def _create_boleto(self, debitId, governmentId, debtAmount, debtDueDate):
        logger.info(f'Creating boleto debitId: {debitId} governmentId: {governmentId} debtAmount: {debtAmount} debtDueDate: {debtDueDate}')
        cod_boleto = uuid4()
        return cod_boleto

    def _send_email(self, name, email, boleto):
        logger.info(f'Sending email name: {name} email: {email} boleto: {boleto}')
        return True
    
    @classmethod
    def delete_byid(cls, debtId):
        try:
            session = postgsql.set_session()
            session.query(cls).filter(cls.debtId==debtId).delete()
            session.commit()
            session.flush()
        except Exception as e:
            logger.error(f'Debt not found {e}')