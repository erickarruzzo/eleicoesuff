from django.conf.urls import url
from eleicoes2018.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^get_candidatos$', get_candidatos, name='get_candidatos'),
    url(r'^get_estados$', get_estados, name='get_estados'),
    url(r'^get_partidos$', get_partidos, name='get_partidos'),
    url(r'^get_cargos$', get_cargos, name='get_cargos'),
    url(r'^busca_candidato$', busca_candidato, name='busca_candidato'),
]
