from django.conf.urls import url
from info_candidatos.views import *

urlpatterns = [
    url(r'^info-registrar$',  RegistrarInfoView.as_view(), name='registrar_info'),
]
