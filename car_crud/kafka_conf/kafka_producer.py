from confluent_kafka import Producer
from .conf import kafka

def kafka_produce(message):
    conf = {'bootstrap.servers': f'{kafka.get_bootstrap_server}'}
    producer = Producer(conf)

    producer.produce(f'{kafka.get_topic}', value=str(message))
    producer.flush()