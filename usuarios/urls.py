from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    url(r'^registrar$',  RegistrarUsuarioView.as_view(), name='registrar'),
]
