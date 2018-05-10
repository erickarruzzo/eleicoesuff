from django.conf.urls import url
from boca_de_urna.views import *

urlpatterns = [
    url(r'^boca_de_urna$', boca_de_urna, name='boca_de_urna'),
    url(r'^get_votos_por_cargo$', get_votos_por_cargo, name='get_votos_por_cargo'),
    url(r'^get_votos_por_cargo_estado$', get_votos_por_cargo_estado, name='get_votos_por_cargo_estado'),
    url(r'^get_votos_por_candidato$', get_votos_por_candidato, name='get_votos_por_candidato'),
]
