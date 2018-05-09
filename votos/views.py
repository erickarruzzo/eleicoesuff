from django.shortcuts import render, redirect
from eleicoes2018.models import *
from django.http import JsonResponse
import pdb

def voto(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registrar_voto1.html', { 'usuarios' : usuarios  })

def carregaVoto(request, usuario_id):
    cargos = Cargo.objects.all()
    candidatos = Candidato.objects.all()
    usuario_ativo = Usuario.objects.get(id=usuario_id)
    return render(request, 'registrar_voto2.html', { 'cargos' : cargos , 'candidatos' : candidatos, 'usuario_ativo' : usuario_ativo })



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
