from sqlalchemy import Column, Float, Integer, String

from src.models import base
from src.repositories.postgresql import postgsql
from src.utils.logger import logger
from src.models.debit import Debit


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
        postgsql.insert(self)
        Debit.delete_byid(self.debtId)
        logger.info(f"Credit computed!. {self.debtId} Removed!")