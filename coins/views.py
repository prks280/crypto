from rest_framework import viewsets

from .serializers import *


class CryptoCoinViewSet(viewsets.ModelViewSet):
    queryset = CryptoCoin.objects.all()
    serializer_class = CryptoCoinSerializer


class CryptoDetailViewSet(viewsets.ModelViewSet):
    queryset = CryptoDetail.objects.all()
    serializer_class = CryptoDetailSerializer
