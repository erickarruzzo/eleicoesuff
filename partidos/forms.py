from django import forms
from eleicoes2018.models import Partido

class RegistrarPartidoForm(forms.Form):

    nome_register = forms.CharField(required=True)
    sigla_register = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(RegistrarPartidoForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            partido_existe = Partido.objects.filter(nome=self.data['nome_register']).exists() or Partido.objects.filter(sigla=self.data['sigla_register']).exists()

            if partido_existe:
                self.adiciona_erro('Partido já cadastrado, favor inserir outro.')
                valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
