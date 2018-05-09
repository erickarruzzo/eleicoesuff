from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView, AlterarUsuarioView, usuario, login
from django.urls import path, include


urlpatterns = [
    url(r'^usuario-registrar$', RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    url(r'^usuario-alterar/(?P<usuario_id>.*)$', AlterarUsuarioView.as_view(), name='alterar_usuario'),
    url(r'^usuario/(?P<usuario_id>\d+)$', usuario, name='usuario'),
    path('usuario/', include('django.contrib.auth.urls'))
]

# http://127.0.0.1:8000/usuario/login/