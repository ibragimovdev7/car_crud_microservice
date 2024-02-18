from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from kafka_conf.kafka_producer import kafka_produce


class Cars(models.Model):
    model = models.CharField(max_length=100)
    price = models.FloatField()
    year = models.DateField(auto_now=True)
    milage = models.IntegerField(default=0)

    def __str__(self):
        return f'Car id {self.id}, car model {self.model}'


@receiver(post_save, sender=Cars)
def send_to_kafka(sender, instance, **kwargs):
    message = {
        'id': instance.id,
        'model': instance.model,
        'price': instance.price,
        'year': instance.year,
        'milage': instance.milage
    }

    kafka_produce(message)


@receiver(post_delete, sender=Cars)
def cars_post_delete(sender, instance, **kwargs):
    message = {
        'action': 'delete',
        'id': instance.id,
        'model': instance.model,
        'price': instance.price,
        'year': instance.year,
        'milage': instance.milage
    }

    kafka_produce(message)

@receiver(post_save, sender=Cars)
def cars_post_delete(sender, instance, **kwargs):
    message = {
        'action': 'update',
        'id': instance.id,
        'model': instance.model,
        'price': instance.price,
        'year': instance.year,
        'milage': instance.milage
    }

    kafka_produce(message)


