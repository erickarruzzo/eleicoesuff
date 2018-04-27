from django.conf.urls import url
from partidos.views import RegistrarPartidoView

urlpatterns = [
    url(r'^partido-registrar$',  RegistrarPartidoView.as_view(), name='registrar_partido'),
]
