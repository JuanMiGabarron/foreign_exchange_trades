from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from main_page.views import index
from main_page.views import new_trade


class IndexTest(TestCase):

    def test_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE HTML>'))
        self.assertTrue(html.endswith('</html>'))
        self.assertIn('<title>trades</title>', html)
        self.assertIn('<h4><strong>Booked Trades</strong></h4>', html)
        self.assertIn('<th>SELL CCY</th>', html)


class NewTradeTest(TestCase):

    def test_new_trade_view(self):
        found = resolve('/newtrade/')
        self.assertEqual(found.func, new_trade)

    def test_new_trade_html(self):
        request = HttpRequest()
        response = new_trade(request)
        html = response.content.decode('utf8')
        self.assertIn('<h4><strong>New Trade</strong></h4>', html)
        self.assertIn('<select id="sell_currency" class="form-control">', html)
        self.assertIn('-- select an option --', html)
