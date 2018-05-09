from django.conf.urls import url
from boca_de_urna.views import *

urlpatterns = [
    url(r'^boca_de_urna$', boca_de_urna, name='boca_de_urna'),
    url(r'^get_candidatos$', get_candidatos, name='get_candidatos'),
    url(r'^get_estados$', get_estados, name='get_estados'),
    url(r'^get_partidos$', get_partidos, name='get_partidos'),
    url(r'^get_cargos$', get_cargos, name='get_cargos'),
]
