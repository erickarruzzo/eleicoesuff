from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Partido
from partidos.forms import RegistrarPartidoForm
from django.views.generic.base import View

class RegistrarPartidoView(View):

    template_name = 'registrar_partido.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarPartidoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            #cria o partido
            partido = Partido(nome=dados_form['nome_register'],
                                sigla=dados_form['sigla_register'])
            #grava no banco
            partido.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
