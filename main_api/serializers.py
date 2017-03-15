from main_page.models import Trade
from rest_framework import serializers


# We use serializers from models and select the fields showed by the api
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = (
            'sell_currency', 'sell_amount', 'buy_currency',
            'buy_amount', 'rate', 'date_booked'
        )
