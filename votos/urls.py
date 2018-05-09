from django.conf.urls import url
from votos.views import *

urlpatterns = [
    url(r'^voto$', carregaVoto, name='voto_carregado'),
    url(r'^voto-registrar$', realiza_voto, name='realiza_voto'),
]
