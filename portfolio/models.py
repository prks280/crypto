from django.db import models
from coins.models import CryptoCoin


class MyPortfolio(models.Model):
    user = models.CharField(max_length=20)  # todo add user
    crypto_coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)
    volume = models.FloatField(default=0.00)


class PortfolioValue(models.Model):
    value = models.FloatField(default=0.00)
