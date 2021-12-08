from rest_framework import serializers

from .models import *


class MyPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPortfolio
        fields = '__all__'


class PortfolioValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioValue
        fields = '__all__'
