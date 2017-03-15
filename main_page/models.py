from __future__ import unicode_literals

from django.db import models
from random import choice


# we store all the alphanumeric values to avoid a lot of calls throw string
cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


# Trade model
class Trade(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    sell_currency = models.CharField(max_length=3)
    sell_amount = models.DecimalField(max_digits=14, decimal_places=2)
    buy_currency = models.CharField(max_length=3)
    buy_amount = models.DecimalField(max_digits=14, decimal_places=2)
    rate = models.DecimalField(max_digits=20, decimal_places=14)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    # save method its called when a value is created or updated
    # we know if object is created by checking the id
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                pkgen = self.pkgen(7)
                if not Trade.objects.filter(id=pkgen):
                    self.id = pkgen
                    super(Trade, self).save(*args, **kwargs)
                    break

    # method to generate the RT******* value
    def pkgen(self, N):
        return 'TR{}'.format(''.join(choice(cases) for i in range(N)))
