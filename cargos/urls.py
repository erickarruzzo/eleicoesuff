from django.conf.urls import url
from cargos.views import RegistrarCargoView

urlpatterns = [
    url(r'^cargo-registrar$',  RegistrarCargoView.as_view(), name='registrar_cargo'),
]
