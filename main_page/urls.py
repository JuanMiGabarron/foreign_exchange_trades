from django.conf.urls import url
from main_page.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]