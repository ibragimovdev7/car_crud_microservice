from confluent_kafka import Consumer, KafkaError
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Document, Keyword, Text
from .conf import kafka


class CarsIndex(Document):
    model = Keyword()
    price = Text()
    year = Text()
    milage = Text()

    class Index:
        name = 'car_list'

#Bu fayl serverda aloxida portda run bo'lib turadi

def kafka_consume():
    conf = {'bootstrap.servers': f'{kafka.get_bootstrap_server}', 'auto.offset.reset': 'earliest'}
    consumer = Consumer(conf)
    consumer.subscribe([f'{kafka.get_topic}'])
    es = Elasticsearch(['http://localhost:9200'])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        payload = eval(msg.value().decode('utf-8'))

        document = CarsIndex(**payload)
        document.save(using=es)

if __name__ == "__main__":
    kafka_consume()