from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import *
from local_votacao.forms import RegistrarLocalForm
from django.views.generic.base import View
from django.http import JsonResponse
import pdb

class RegistrarLocalView(View):

    template_name = 'registrar_local.html'

    def get(self, request, *args, **kwargs):
        estados = Estado.objects.all()
        return render(request, self.template_name, { "estados" : estados })

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarLocalForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            estado = Estado.objects.get(id=dados_form['estado_register'])

            #cria o Local
            local = LocalVotacao(zona=dados_form['zona_register'], secao=dados_form['secao_register'], endereco=dados_form['endereco_register'], estado=estado, mapa=dados_form['mapa_register'])

            #grava no banco
            local.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

def local(request):
    estados = Estado.objects.all()
    return render(request, 'local_consulta.html', { "estados" : estados })

def get_local_votacao(request, *a, **kw):
    titulo = request.GET.get("titulo", None)
    estado = request.GET.get("estado", None)

    #pdb.set_trace()

    soma = sum(int(i) for i in titulo)
    
    if soma <= 54:
        local = LocalVotacao.objects.get(estado_id=estado, zona__lte=108)
    else:
        local = LocalVotacao.objects.get(estado_id=estado, zona__gt=108)

    response = { 
                'id' : local.id,
                'estado' : local.estado.nome,
                'endereco' : local.endereco,
                'secao' : local.secao,
                'zona' : local.zona,
                'mapa' : local.mapa
                }

    return JsonResponse(response)
