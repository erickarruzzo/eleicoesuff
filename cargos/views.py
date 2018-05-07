from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Cargo
from cargos.forms import RegistrarCargoForm
from django.views.generic.base import View

class RegistrarCargoView(View):

    template_name = 'registrar_cargo.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarCargoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            #cria o cargo
            cargo = Cargo(nome=dados_form['nome_register'])
            
            #grava no banco
            cargo.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
