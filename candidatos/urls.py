from django.conf.urls import url
from candidatos.views import RegistrarCandidatoView

urlpatterns = [
    url(r'^candidato-registrar$',  RegistrarCandidatoView.as_view(), name='registrar_candidato'),
]
