from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('eleicoes2018.urls')),
    url(r'^', include('usuarios.urls')),
    url(r'^', include('partidos.urls')),
    url(r'^', include('estados.urls')),
    url(r'^', include('cargos.urls')),
    url(r'^', include('candidatos.urls')),
    url(r'^', include('votos.urls')),
    url(r'^', include('boca_de_urna.urls')),
    url(r'^', include('info_candidatos.urls')),
    url(r'^', include('info_cargos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
