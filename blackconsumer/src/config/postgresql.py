import os


class PostgreSQLConfig:
    ''' Elasticsearch Settings
    '''
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')
    USER = os.environ.get('DB_USER')
    PASS = os.environ.get('DB_PASS')
    
    def __init__(self):
        self._validate_host()
        self._validate_port()
        self._validate_user()
        self._validate_pass()

    def _validate_host(self):
        if self.HOST is None:
            raise ValueError("DB_HOST should not be empty")

    def _validate_port(self):
        if self.PORT is None:
            raise ValueError("DB_PORT should not be empty")

    def _validate_user(self):
        if self.USER is None:
            raise ValueError("DB_USER should not be empty")

    def _validate_pass(self):
        if self.PASS is None:
            raise ValueError("DB_PASS should not be empty")