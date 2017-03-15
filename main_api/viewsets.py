from main_page.models import Trade
from main_api.serializers import TradeSerializer
from rest_framework.viewsets import ModelViewSet


# viewset of the api, the display all the object ordered by date_booked
class TradeViewSet(ModelViewSet):
    queryset = Trade.objects.all().order_by('-date_booked')
    serializer_class = TradeSerializer
