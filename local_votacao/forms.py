from django import forms
from eleicoes2018.models import *


class RegistrarLocalForm(forms.Form):

    zona_register = forms.IntegerField(required=True)
    secao_register = forms.IntegerField(required=True)
    endereco_register = forms.CharField(required=True)
    estado_register = forms.CharField(required=True)
    mapa_register = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(RegistrarLocalForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            local_existe = LocalVotacao.objects.filter(endereco=self.data['endereco_register']).exists()

            if local_existe:
                self.adiciona_erro('Local de votação já cadastrado, favor inserir outro.')
                valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
