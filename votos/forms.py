from django import forms
from eleicoes2018.models import Voto, Candidato, Usuario

class RegistrarVotoForm(forms.Form):

    usuario_register = forms.CharField(required=True)
    candidato_register = forms.CharField(required=True)

    def is_valid(self):
            valid = True
            #if not super(RegistrarVotoForm, self).is_valid():
            #    self.adiciona_erro('Por favor, verifique os dados informados')
            #    valid = False

            #votos = Voto.objects.all()
            #candidato_voto = Candidato.objects.get(id=self.data['candidato_register'])

            #voto_existe = False

            #for voto in votos:
            #    if voto.usuario_id == self.data['usuario_register'] and voto.candidato_id.cargo_id = candidato_voto.cargo_id:
            #        voto_existe = True

            #if voto_existe:
            #    self.adiciona_erro('Voto já cadastrado para este cargo.')
            #    valid = False

            return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
