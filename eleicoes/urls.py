from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('eleicoes2018.urls')),
    url(r'^', include('usuarios.urls')),
    url(r'^', include('partidos.urls')),
    url(r'^', include('estados.urls')),
]
