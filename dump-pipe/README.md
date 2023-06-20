# Dump Pipe Hands on Tutorial

In this hands-on tutorial we will start a [kafka](https://kafka.apache.org/) docker container and run scripts to send and receive events. We will also visualize what happens in the Confluenct management panel.

The purpose is to get more familiar with dump pipe techonlogie

## Run containers

Make sure you have [docker](https://docs.docker.com/get-docker/) installed and running on your machine.
Then run the following command in the root of this project:

```bash
docker compose up -d
```

This will start a few containers:

* `broker`: the kafka broker running topics
* `kafka-ui`: a UI to visualize topics
* `kafka_scripts`: custom script we will run

## Management panel

The Kafka management panel can be [accessed](http://localhost:9000)

the control pannel will give you access to a general overview of the kafka broker

## Scripts container

We will use the script container to execute some example scenarios to use Kafka. In your console/terminal connect to the scripts container.

```bash
docker exec -it kafka_scripts bash
```

Now you are connected to the container and can run the scripts in the `dump-pipe/src` folder. You should open several consoles/terminals to run multiple scripts at the same time. So lets open 1 new console/terminal and connect to the scripts container again.

## Send and receive messages

In the first console/terminal run the following command:

```bash
./helloproducer.py
```

the helloproducer will create a topic if it does not exist and send messages to the topic `postnl` every few seconds. let check the kafka management panel to see the topic, feel free to explore.

```bash
http://localhost:9000/
```

When you click the `postnl` topic you can also see how many partitions are in the topic. the messages are hashed by key and send to a partition. Lets see the messsage by pressing the `view messages` button. select partition 0 and click on the `view messages` button. Now do the same for partition 1.

Now in the second console/terminal run the following command:

```bash
./helloconsumer.py
```

Do you get all the messages?

## sharing messages

Keep the previous consumer and producer running and start two new terminals (named 3 and 4)

```bash
docker exec -it kafka_scripts bash
```

In terminal 3 start the consumer again

```bash
./helloconsumer.py
```

Now check the output of the consumers. Do the consumers get all the messages? In terminal 4 start the consumer again

```bash
./helloconsumer.py
```

Why do not all the consumers get messages?

lets stop one of the consumers and restart it in a new consumer group `test`. You can stop the helloconsumer  by pressing `ctrl+c` in the console/terminal.

```bash
./helloconsumer.py -g "test"
```

Why did you get so many messages for the new consumer?

Lets close all the consumer by pressing `ctrl+c` in the console/terminal

## Materialed view

In this part we are going to create a new topic with a special cleanup policy. there are 2 kafka broker cleanup policies:

```bash
cleanup.policy=compact
cleanup.policy=delete # default
```

with `delete` all messages after 1 week (default) are deleted. with compact Kafka only stores the most recent value for each key in the topic. we will create a new compact topic.

lets open a new terminal/console and connect to the **kafka broker** container

```bash
docker exec -it kafka-broker bash
```

then create a new topic `postnl-compact` with settings that will remove all messages with the same key that are older then 5 seconds

```bash
kafka-topics --bootstrap-server localhost:9092 --create --topic postnl-compact --partitions 2 --replication-factor 1  --config cleanup.policy=compact --config min.cleanable.dirty.ratio=0.001 --config segment.ms=5000
```

Now start 3 new terminals and connect to the scripts container.

```bash
docker exec -it kafka_scripts bash
```

in terminal 1 start the producer

```bash
./helloproducer.py -t postnl-compact
```

Let go to the management panel and see what is happening to the topic `postnl-compact`. [link](http://localhost:9000/topic/postnl-compact). press on one of the 2 partitions and keep refreshing the results by pressing `view messages`

Can you see the messages disappearing for a partion? this is the cleanup process that is running. This system allows you to always keep the latest message of a given key without needing infinate storage.

## cleanup containers and volumes

When you are done with the hands-on you can stop the containers and remove the volumes by running the following command in the folder dump-pipe of this project:

```bash
docker compose down -v
```

## Other Resources
* [KSQL]S(https://www.confluent.io/product/ksqldb)
