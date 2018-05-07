from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Estado
from estados.forms import RegistrarEstadoForm
from django.views.generic.base import View

class RegistrarEstadoView(View):

    template_name = 'registrar_estado.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarEstadoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            #cria o estado
            estado = Estado(nome=dados_form['nome_register'],
                                sigla=dados_form['sigla_register'])
            #grava no banco
            estado.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
