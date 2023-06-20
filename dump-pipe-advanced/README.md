# Dump Pipe advanced Hands on Tutorial

Welcome to the Advanced Hands on! here we will play with the full capabilities of the kafka confluent platform. Confluent is a company that comerialized the kafka platform by selling additional features and giving support for kafka.

## Run containers

Make sure you have [docker](https://docs.docker.com/get-docker/) installed and running on your machine.
Then run the following command in the root of this project:

```bash
docker compose up -d
```

This will start a few containers it may take a few minutes for everything to be up and running
|service|description|
|---|---|
|Confluent Schema Registry| schema registry for producers to send schemas, they can be enforced by the broker|
|Kafka Connect| centralized data hub for simple data integration between databases, key-value stores, search indexes, and file systems |
|Confluent Control Center| eb-based tool for managing and monitoring Apache Kafka |
|ksqlDB| SQL on data streams |
|Confluent REST Proxy| rest proxy for kafka |

## Confluent example (kSQLdb, rest, connect and schema registry)

Now follow the manual from [confluent](https://docs.confluent.io/platform/current/platform-quickstart.html#step-2-create-ak-topics-for-storing-your-data)

## kafka streams

Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in an Apache Kafka® cluster. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka's server-side cluster technology. unfortunalty i did not have time to prepare anything for this. feel free to follow the following documentation:

https://docs.confluent.io/platform/current/streams/overview.html
