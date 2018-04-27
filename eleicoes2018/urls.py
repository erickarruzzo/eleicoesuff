from django.conf.urls import url
from eleicoes2018.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
