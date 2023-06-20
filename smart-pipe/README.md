# Smart Pipe Hands on Tutorial

In this hands-on tutorial we will start a [rabbitMQ](https://www.rabbitmq.com/getstarted.html) docker container and run scripts to send and receive messages using different type of [exchanges](https://www.rabbitmq.com/tutorials/amqp-concepts.html). We will also visualize what happens in the rabbitMQ management panel.

The purpose is to get more familiar with smart pipe techonlogie

## Run containers

Make sure you have [docker](https://docs.docker.com/get-docker/) installed and running on your machine.
Then run the following command in the smart-pipe folder of this project:

```bash
docker compose up -d
```

This will start 2 containers named `rabbitmq` and `rabbitmq_scripts`. It may take a minute for everything to start.

## Management panel

RabbitMQ supports a management panel which can be [accessed](http://localhost:15672):

```bash
http://localhost:15672
```

For credentials use:
|         |            |
| ------------- |-------------|
|username | **postnl**
|password | **postnl**

This will give you access to the RabbitMQ contral panel. For this handson only the [Queues](http://localhost:15672/#/queues) tab and [Exchanges](http://localhost:15672/#/exchanges) tab is of interest. But feel free to explore more.

### Exchanges

In the `Exchanges` tab you can see the different exchanges that are created by the scripts we will run. For now it contains the default exchanges that are created by rabbitMQ. You can try and create a new exchange by clicking the `Add a new exchange` button. but it not necessary for this hands-on.

When you click on an exchange, for example the `amq.direct` exchange you can publish messages to it. If there is no queue attached the message will be lost. The binding section shows which queues are bound to the exchange.

### Queues

In the `Queues` tab you can see the different queues that are created by the scripts we will run. By default no queues are created. You can try and create a new queue by clicking the `Add a new queue` button. You could create the `hello` queue and bind it to the `amq.direct` exchange with the routing key `hello`. But this is not necessary for this hands-on.

When you click on a queue, for example the `hello` queue you can publich messages to is, get messages or purge the queue. The binding section shows which exchanges are bound to the queue.

## Scripts container

We will use the script container to execute some example scenarios to use rabbitMQ. In your console/terminal connect to the scripts container.

```bash
docker exec -it rabbitmq_scripts bash
```

Now you are connected to the container and can run the scripts in the `src` folder. You should open several consoles/terminals to run multiple scripts at the same time. So lets open a new console/terminal and connect to the scripts container again.

## Send and receive messages with basic exchange

In the first console/terminal run the following command:

```bash
./helloconsumer.py
```

This will receive the message from the `hello` queue. if you now look in the management panel you can see the queue \

Now in the second console/terminal run the following command:

```bash
./helloproducer.py
```

This will send a message to the `hello` queue. check this by looking the the first console/terminal \

stop the `helloconsumer.py` and `helloproducer.py` script by pressing `ctrl+c` in the console/terminal.\

## filter messages with basic exchange

In the first console/terminal run the following command:

```bash
./routingconsumer.py info warning
```

this will listen for message that contain the key `info` or `warning` and print the message to the console.

in the second console/terminal run the following commands:

```bash
./routingproducer.py info
./routingproducer.py error
./routingproducer.py warning
```

this will send messages with different keys to the exchange. The first command will send a message with the key `info`. The second command will send a message with the key `error`. The third command will send a message with the key `warning`. check the output of the first console/terminal to see which messages are received.

stop the `routingconsumer.py` and `routingproducer.py` script by pressing `ctrl+c` in the first console/terminal.

## Filtering messages with topic exchanges

In the first console/terminal run the following command:

```bash
./topicconsumer.py "*.critical"
```

this will listen for message that contain the key `info` or `warning` and print the message to the console.

in the second console/terminal run the following commands:

```bash
./topicproducer.py "postnl.critical" "A critical error"
./topicproducer.py "sbp.critical" "A critical error"
./topicproducer.py "sbp.info" "A info message"
```

this will send messages with different keys to the exchange. why did we not receive the sbp.info message in the consumer?

stop the `routingconsumer.py` script by pressing `ctrl+c` in the first console/terminal.

## Cleanup containers and volumes

When you are done with the hands-on you can stop the containers and remove the volumes by running the following command in the folder smart-pipe of this project:

```bash
docker compose down -v
```
