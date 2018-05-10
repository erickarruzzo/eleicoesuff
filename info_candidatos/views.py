from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import *
from info_candidatos.forms import RegistrarInfoForm
from django.views.generic.base import View

class RegistrarInfoView(View):

    template_name = 'registrar_info.html'

    def get(self, request, *args, **kwargs):
        candidatos = Candidato.objects.all()
        return render(request, self.template_name, { 'candidatos' : candidatos })

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarInfoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            candidato = Candidato.objects.get(id=dados_form['candidato_register'])

            #cria a info
            info = Info(texto=dados_form['info_register'],candidato_id=candidato)

            #grava no banco
            info.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
