from django.conf.urls import url
from boca_de_urna.views import *

urlpatterns = [
    url(r'^boca_de_urna$', boca_de_urna, name='boca_de_urna'),
]
