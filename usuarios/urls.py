from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView, usuario, login

urlpatterns = [
    url(r'^registrar$',  RegistrarUsuarioView.as_view(), name='registrar'),
    url(r'^usuario/(?P<usuario_id>\d+)$', usuario, name='usuario'),
    url(r'^login$', login, name='login')
]
