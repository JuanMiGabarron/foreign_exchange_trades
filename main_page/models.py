from __future__ import unicode_literals

from django.db import models

#Trade model
class Trade(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    sell_currency = models.CharField(max_length=3)
    sell_amount = models.DecimalField(max_digits=8, decimal_places=2)
    buy_currency = models.TextField(max_length=3)
    buy_amount = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=4)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
