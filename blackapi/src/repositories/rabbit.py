from pika import ConnectionParameters, BlockingConnection, PlainCredentials
import os

class Rabbit:
    def __init__(self) -> None:
        self.credentials = PlainCredentials(
            username=os.environ['RABBITMQ_DEFAULT_USER'], 
            password=os.environ['RABBITMQ_DEFAULT_PASS']
        )

        self.parameters = ConnectionParameters('rabbitmq',
                                       5672,
                                       '/',
                                       self.credentials)

        self.connection = BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def send_message(self, queue, routing_key, body):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='',
                            routing_key=routing_key,
                            body=body)

        return True

