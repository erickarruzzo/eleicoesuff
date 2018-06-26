from django.conf.urls import url
from info_cargos.views import *

urlpatterns = [
    url(r'^cargo/(?P<cargo_id>\d+)$', cargo, name='cargo'),
]
