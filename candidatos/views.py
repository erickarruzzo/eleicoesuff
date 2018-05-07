from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Candidato, Estado, Partido, Cargo
from candidatos.forms import RegistrarCandidatoForm
from django.views.generic.base import View

class RegistrarCandidatoView(View):

    template_name = 'registrar_candidato.html'

    def get(self, request, *args, **kwargs):
        estados = Estado.objects.all()
        partidos = Partido.objects.all()
        cargos = Cargo.objects.all()
        return render(request, self.template_name, { 'estados' : estados , 'partidos' : partidos , 'cargos' : cargos })

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarCandidatoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            partido = Partido.objects.get(id=dados_form['partido_register'])
            estado = Estado.objects.get(id=dados_form['estado_register'])
            cargo = Cargo.objects.get(id=dados_form['cargo_register'])

            #cria o candidato
            candidato = Candidato(nome=dados_form['nome_register'],
                                partido_id=partido,
                                estado_id=estado,
                                cargo_id=cargo)
            #grava no banco
            candidato.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
