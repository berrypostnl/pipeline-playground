#!/usr/bin/env python
import sys

import pika

credentials = pika.credentials.PlainCredentials("postnl", "postnl")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq", credentials=credentials, virtual_host="postnl")
)
channel = connection.channel()

channel.exchange_declare(exchange="postnl_logs", exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="postnl_logs", routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
