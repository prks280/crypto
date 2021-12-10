from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('coin', CryptoCoinViewSet)
router.register('details', CryptoDetailViewSet)

urlpatterns = router.urls
