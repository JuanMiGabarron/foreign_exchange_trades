from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from main_api.viewsets import TradeViewSet


class APITest(TestCase):

    def test_api_viewset(self):
        found = resolve('/api/trades/')
        self.assertEqual(found.func, TradeViewSet)

    def test_api_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE HTML>'))
        self.assertTrue(html.endswith('</html>'))
        self.assertIn('<b>HTTP 200 OK</b>', html)
