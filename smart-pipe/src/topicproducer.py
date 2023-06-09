#!/usr/bin/env python
import sys

import pika

credentials = pika.credentials.PlainCredentials("postnl", "postnl")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq", credentials=credentials, virtual_host="postnl")
)
channel = connection.channel()

channel.exchange_declare(exchange="postnl_logs2", exchange_type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 2 else "anonymous.info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="postnl_logs2", routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
