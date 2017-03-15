from django.conf.urls import url, include
from rest_framework import routers
from main_api.viewsets import TradeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('trades', TradeViewSet, 'trade')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
