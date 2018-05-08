from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView, AlterarUsuarioView, usuario, login

urlpatterns = [
    url(r'^usuario-registrar$', RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    url(r'^usuario-alterar/(?P<usuario_id>.*)$', AlterarUsuarioView.as_view(), name='alterar_usuario'),
    url(r'^usuario/(?P<usuario_id>\d+)$', usuario, name='usuario'),
    url(r'^login/$', login, name='login')
]
