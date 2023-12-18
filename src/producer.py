import json
from datetime import datetime
from models import Contact

import pika

from faker import Faker

fake = Faker("uk-UA")

credentials = pika.PlainCredentials(username="guest", password="guest")

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

exchange = "pyweb-hw-08 Service"
queue = "pyweb-hw-08_campaign"


channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue, durable=True)
channel.queue_bind(exchange=exchange, queue=queue)


def create_tasks(nums: int):
    for i in range(nums):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
        ).save()

        channel.basic_publish(
            exchange=exchange,
            routing_key=queue,
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(f" [x] Sent '{contact.id}'")

    connection.close()


if __name__ == "__main__":
    create_tasks(10)
