#!/usr/bin/env python
import argparse
import sys

from confluent_kafka import Consumer, KafkaError, KafkaException


def main(args):
    conf = {
        "bootstrap.servers": args.bootstrap_servers,  # comma seperated list of brokers to connnect to
        "group.id": args.group_id,  # group the consumer is part of
        "auto.offset.reset": "smallest",
    }  # property specifies what offset the consumer should start reading from in the event there are no committed offsets for a partition, or the committed offset is invalid

    consumer = Consumer(conf)
    topics = ["postnl"]  # comma seperated list of topics to subscribe to

    print("Producing records from topic {}. ^C to exit.".format(topics))
    try:
        consumer.subscribe(topics)

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        "%% %s [%d] reached end at offset %d\n" % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.key(), msg.value())
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="example")
    parser.add_argument(
        "-b",
        dest="bootstrap_servers",
        default="broker:29092",
        help="Bootstrap broker(s) (host[:port])",
    )
    parser.add_argument(
        "-g",
        dest="group_id",
        default="postnl",
        help="Schema Registry (http(s)://host[:port]",
    )
    parser.add_argument("-t", dest="topic", default="postnl", help="Topic name")
    parser.add_argument("-o", dest="offset", default="smallest", help="offset reset stratigy name")

    main(parser.parse_args())
