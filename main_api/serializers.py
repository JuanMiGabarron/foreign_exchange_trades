from main_page.models import Trade
from rest_framework import serializers


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('sell_currency', 'sell_amount', 'buy_currency', 'buy_amount', 'rate', 'date_booked')
