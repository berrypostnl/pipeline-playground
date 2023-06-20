FROM python:3.11

RUN pip install  --no-cache-dir confluent_kafka 

WORKDIR /usr/src/scripts

COPY src/ .

CMD [ "/bin/bash", "-c", "sleep infinity" ]