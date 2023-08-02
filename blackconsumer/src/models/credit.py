from sqlalchemy import Column, Float, Integer, String, DateTime

from src.models import base
from src.repositories.postgresql import postgsql
from src.utils.logger import logger
from src.models.debit import Debit


class Credit(base):
    __tablename__ = 'Credits'
    debtId = Column(Integer, primary_key=True)
    paidAt = Column(DateTime)
    paidAmount = Column(Float)
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