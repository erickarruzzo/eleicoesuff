from django.conf.urls import url
from eleicoes2018.views import index, usuario, login

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^usuario/(?P<usuario_id>\d+)$', usuario, name='usuario'),
    url(r'^login$', login, name='login')
]