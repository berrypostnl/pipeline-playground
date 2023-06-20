FROM python:3.11

#RUN apt-get install librdkafka-dev
#RUN apt-get update && apt-get install -y \
#    librdkafka \
#    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pika

WORKDIR /usr/src/scripts

COPY src/ .

CMD [ "/bin/bash", "-c", "sleep infinity" ]