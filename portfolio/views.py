from rest_framework import viewsets

from .serializers import *


class MyPortfolioViewSet(viewsets.ModelViewSet):
    queryset = MyPortfolio.objects.all()
    serializer_class = MyPortfolioSerializer


class PortfolioValueViewSet(viewsets.ModelViewSet):
    queryset = PortfolioValue.objects.all()
    serializer_class = PortfolioValueSerializer
