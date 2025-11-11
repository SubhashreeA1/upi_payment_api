import pika
from django.conf import settings

def get_connection():
    credentials = pika.PlainCredentials(settings.RABBITMQ["USER"], settings.RABBITMQ["PASSWORD"])
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ["HOST"], port=settings.RABBITMQ["PORT"], credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ["QUEUE"], durable=True)
    return connection, channel
