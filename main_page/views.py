from django.shortcuts import render
from django.utils import timezone

currencies = [
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK",
    "EUR", "GBP", "HKD", "HRK", "HUF", "IDR", "ILS", "INR",
    "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN",
    "RON", "RUB", "SEK", "SGD", "THB", "TRY", "USD", "ZAR"
]

# Create your views here.
def index(request):
    return render(request, 'main_page/index.html')

def new_trade(request):
    return render(request,
        'main_page/new_trade.html',
        {'currencies': currencies}
    )
