from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView, usuario, login

urlpatterns = [
    url(r'^usuario-registrar$',  RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    url(r'^usuario/(?P<usuario_id>\d+)$', usuario, name='usuario'),
    url(r'^login/$', login, name='login')
]
