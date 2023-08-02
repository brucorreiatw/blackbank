from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.postgresql import PostgreSQLConfig


class Postgresql:
    def __init__(self):
        self.config = PostgreSQLConfig()
        self.db = self._create_engine()

    def _create_engine(self):
        db_string = f'postgresql://{self.config.USER}:{self.config.PASS}@{self.config.HOST}:{self.config.PORT}/blackbank'
        return create_engine(db_string)

    def set_session(self):
        Session = sessionmaker(self.db, expire_on_commit=False)
        return Session()

    def insert(self, operation):
        session = self.set_session()
        session.add(operation)
        session.commit()
        session.flush()
    
    # def select(self, query):
    #     session = self.set_session()
    #     return session.execute(query).fetchall()

postgsql = Postgresql()