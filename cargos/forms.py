from django import forms
from eleicoes2018.models import Cargo

class RegistrarCargoForm(forms.Form):

    nome_register = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(RegistrarCargoForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            cargo_existe = Cargo.objects.filter(nome=self.data['nome_register']).exists()

            if cargo_existe:
                self.adiciona_erro('Cargo já cadastrado, favor inserir outro.')
                valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
