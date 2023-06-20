#!/usr/bin/env python
import pika

credentials = pika.credentials.PlainCredentials("postnl", "postnl")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq", credentials=credentials, virtual_host="postnl")
)
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

print(" [x] Sent 'Hello World!'")

connection.close()
