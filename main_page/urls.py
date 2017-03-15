from django.conf.urls import url
from main_page.views import index
from main_page.views import new_trade

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^newtrade/$', new_trade, name='new_trade'),
]
