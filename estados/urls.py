from django.conf.urls import url
from estados.views import RegistrarEstadoView

urlpatterns = [
    url(r'^estado-registrar$',  RegistrarEstadoView.as_view(), name='registrar_estado'),
]
