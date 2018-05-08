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

class AlterarUsuarioForm(forms.Form):

    id_perfil = forms.IntegerField(required=True)
    cpf_perfil = forms.CharField(required=True)
    nome_perfil = forms.CharField(required=True)
    email_perfil = forms.EmailField(required=True)
    estado_perfil = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            if not super(AlterarUsuarioForm, self).is_valid():
                self.adiciona_erro('Por favor, verifique os dados informados')
                valid = False

            myuser = Usuario.objects.get(id=self.data['id_perfil'])

            usuario_existe = myuser.cpf != self.data['cpf_perfil'] and Usuario.objects.filter(cpf=self.data['cpf_perfil']).exists()

            if usuario_existe:
                self.adiciona_erro('CPF já cadastrado, favor inserir outro.')
                valid = False

            if(len(self.data['cpf_perfil']) != 11):
                self.adiciona_erro('CPF precisa ter 11 numeros')
                valid = False


            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
