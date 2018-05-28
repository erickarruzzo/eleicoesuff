from django.conf.urls import url
from candidatos.views import *

urlpatterns = [
    url(r'^candidatos$',  candidatos, name='candidatos'),
    url(r'^candidato-registrar$',  RegistrarCandidatoView.as_view(), name='registrar_candidato'),
    url(r'^candidato/(?P<candidato_id>\d+)$', candidato, name='candidato'),
    url(r'^get_candidatos_com_filtro$', get_candidatos_com_filtro, name='get_candidatos_com_filtro'),
]
