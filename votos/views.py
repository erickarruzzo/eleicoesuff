from django.shortcuts import render, redirect
from eleicoes2018.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import pdb

@login_required
def carregaVoto(request):
    current_user = request.user
    #pdb.set_trace()
    cargos = Cargo.objects.all()
    candidatos = Candidato.objects.all()
    usuario_ativo = Usuario.objects.get(id=current_user.id)
    return render(request, 'registrar_voto2.html', { 'cargos' : cargos , 'candidatos' : candidatos, 'usuario_ativo' : usuario_ativo })


@csrf_exempt
@login_required
def realiza_voto(request, *a, **kw):
    # Notice I didn't directly try to access request.GET["check_this"]
    #code.interact(local=dict(globals(), **locals()))
    usuario_id = request.POST.get("usuario_id", None)
    candidato_id = request.POST.get("candidato_id", None)

    #pdb.set_trace()

    usuario = Usuario.objects.get(id=usuario_id)
    candidato = Candidato.objects.get(id=candidato_id)

    #cria o voto
    voto = Voto(usuario_id=usuario,candidato_id=candidato)

    #grava no banco
    voto.save()

    votos = Voto.objects.all().values()

    list_voto = list(votos)
    return JsonResponse(list_voto, safe=False)
