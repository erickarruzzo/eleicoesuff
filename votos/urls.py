from django.conf.urls import url
from votos.views import voto, realiza_voto, carregaVoto

urlpatterns = [
    url(r'^voto$', voto, name='voto'),
    url(r'^voto/(?P<usuario_id>\d+)$', carregaVoto, name='voto_carregado'),
    url(r'^voto/voto-registrar$', realiza_voto, name='realiza_voto'),
]
