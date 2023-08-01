import os


class RBMQConfig:
    ''' RabbitMQ Settings
    '''
    HOST = os.environ.get('RBMQ_HOST')
    PORT = os.environ.get('RBMQ_PORT')
    USER = os.environ.get('RBMQ_USER')
    PASS = os.environ.get('RBMQ_PASS')
    INVOICE_QUEUE = os.environ.get('INVOICE_QUEUE')

    def __init__(self):
        self._validate_host()
        self._validate_port()
        self._validate_user()
        self._validate_pass()

    def _validate_host(self):
        if self.HOST is None:
            raise ValueError("RBMQ_HOST should not be empty")
    
    def _validate_port(self):
        if self.PORT is None:
            raise ValueError("RBMQ_PORT should not be empty")

    def _validate_user(self):
        if self.USER is None:
            raise ValueError("RBMQ_USER should not be empty")

    def _validate_pass(self):
        if self.PASS is None:
            raise ValueError("RBMQ_PASS should not be empty")

