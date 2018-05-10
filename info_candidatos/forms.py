from django import forms
from eleicoes2018.models import *

class RegistrarInfoForm(forms.Form):

    info_register = forms.CharField(required=True)
    candidato_register = forms.CharField(required=True)


    def is_valid(self):
            valid = True
            if not super(RegistrarInfoForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
