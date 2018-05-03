from django import forms
from eleicoes2018.models import Usuario

class RegistrarUsuarioForm(forms.Form):

    cpf_register = forms.CharField(required=True)
    nome_register = forms.CharField(required=True)
    email_register = forms.EmailField(required=True)
    estado_register = forms.CharField(required=True)
    senha_register1 = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(RegistrarUsuarioForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            usuario_existe = Usuario.objects.filter(cpf=self.data['cpf_register']).exists()

            if usuario_existe:
                self.adiciona_erro('CPF já cadastrado, favor inserir outro.')
                valid = False

            if(len(self.data['cpf_register']) != 11):
                self.adiciona_erro('CPF precisa ter 11 numeros')
                valid = False


            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
