from django.conf.urls import url
from resultado.views import *

urlpatterns = [
    url(r'^resultado$', resultado, name='resultado'),
]