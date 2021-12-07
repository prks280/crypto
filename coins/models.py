from django.db import models


class CryptoCoin(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_on = models.DateField()
    rank = models.SmallIntegerField(default=0)


class CryptoDetail(models.Model):
    crypto_coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)
    current_price = models.FloatField(default=0.0)
    high_24_hour = models.FloatField(default=0.0)
    low_24_hour = models.FloatField(default=0.0)
    volume_24_hour = models.FloatField(default=0.0)
    market_cap = models.IntegerField(default=0.00)

# just for test
