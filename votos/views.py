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
    usuario_ativo = Usuario.objects.get(email=current_user.username)
    return render(request, 'registrar_voto2.html', { 'cargos' : cargos , 'candidatos' : candidatos, 'usuario_ativo' : usuario_ativo })


@csrf_exempt
@login_required
def realiza_voto(request, *a, **kw):
    usuario_id = request.POST.get("usuario_id", None)
    candidato_id = request.POST.get("candidato_id", None)

    #pdb.set_trace()

    usuario = Usuario.objects.get(id=usuario_id)
    candidato = Candidato.objects.get(id=candidato_id)

    ja_votei = Voto.objects.filter(usuario=usuario.id, candidato__cargo_id=candidato.cargo_id).exists()

    if ja_votei:
        response = { 'response' : '0' }
        return JsonResponse(response)

    #cria o voto
    voto = Voto(usuario=usuario,candidato=candidato)

    #grava no banco
    voto.save()

    response = { 'response' : '1' }

    return JsonResponse(response)
