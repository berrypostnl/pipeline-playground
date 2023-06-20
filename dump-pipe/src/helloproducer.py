#!/usr/bin/env python
import argparse
import random
import time

from confluent_kafka import Producer


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s %s" % (str(msg.key()), str(msg.value())))


def main(args):
    conf = {"bootstrap.servers": args.bootstrap_servers}
    topic = args.topic

    dictionary = {
        "berry": "amsterdam",
        "luc": "rotterdam",
        "seluc": "the hague",
        "bas": "zandvoort",
    }

    producer = Producer(conf)

    print("Producing records to topic {}. ^C to exit.".format(topic))
    while True:
        try:
            key = random.choice(list(dictionary.keys()))

            producer.produce(
                topic, key=key, value=dictionary[key], callback=acked
            )  # produe a message to the topic postnl
            producer.flush()  # make syncronous instead of asyncronous
            time.sleep(2.5)
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid input, discarding record...")
            continue

    producer.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="example")
    parser.add_argument(
        "-b",
        dest="bootstrap_servers",
        default="broker:29092",
        help="Bootstrap broker(s) (host[:port])",
    )
    parser.add_argument("-t", dest="topic", default="postnl", help="Topic name")

    main(parser.parse_args())
