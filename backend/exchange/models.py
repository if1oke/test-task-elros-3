import random

from django.db import models


class Rates(models.Model):
    ton = models.PositiveIntegerField(
        null=False
    )
    btc = models.PositiveIntegerField(
        null=False
    )

    @staticmethod
    def produce_exchange_rates():
        print(123123)
        Rates(
            ton=random.randint(28400, 43200),
            btc=random.randint(6532200, 6712100)
        ).save()

    @staticmethod
    def get_current_rate():
        return Rates.objects.last()

    @staticmethod
    def get_last_5_rates():
        return Rates.objects.order_by('-id')[:5]
