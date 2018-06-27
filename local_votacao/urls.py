from django.conf.urls import url
from local_votacao.views import *

urlpatterns = [
    url(r'^local-registrar$',  RegistrarLocalView.as_view(), name='registrar_local'),
    url(r'^local-consulta$',  local, name='local'),
    url(r'^get_local_votacao$', get_local_votacao, name='get_local_votacao'),
]