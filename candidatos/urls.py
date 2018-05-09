from django.conf.urls import url
from candidatos.views import *

urlpatterns = [
    url(r'^candidato-registrar$',  RegistrarCandidatoView.as_view(), name='registrar_candidato'),
    url(r'^candidato/(?P<candidato_id>\d+)$', candidato, name='candidato'),
]
