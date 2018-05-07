from django import forms
from eleicoes2018.models import Candidato

class RegistrarCandidatoForm(forms.Form):

    nome_register = forms.CharField(required=True)
    partido_register = forms.CharField(required=True)
    estado_register = forms.CharField(required=True)
    cargo_register = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(RegistrarCandidatoForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            candidato_existe = Candidato.objects.filter(nome=self.data['nome_register']).exists()

            if candidato_existe:
                self.adiciona_erro('Candidato já cadastrado, favor inserir outro.')
                valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
