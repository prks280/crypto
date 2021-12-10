from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('my_coins', MyPortfolioViewSet)
router.register('values', PortfolioValueViewSet)

urlpatterns = router.urls
