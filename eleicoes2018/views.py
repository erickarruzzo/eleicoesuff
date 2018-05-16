from django.shortcuts import render
from django.http import JsonResponse
from eleicoes2018.models import *


def index(request):
    usuarios = Usuario.objects.all()
    estados = Estado.objects.all()
    partidos = Partido.objects.all()
    cargos = Cargo.objects.all()
    candidatos = Candidato.objects.all().order_by('nome')
    noticias = Noticia.objects.all().order_by('-data')
    return render(request, 'index.html', { 'usuarios' : usuarios , 'estados' : estados , 'partidos' : partidos , 'cargos' : cargos , 'candidatos' : candidatos , 'noticias' : noticias })


def get_candidatos(request):
    #pdb.set_trace()
    candidatos = Candidato.objects.all().values()
    list_candidato = list(candidatos)
    return JsonResponse(list_candidato, safe=False)


def get_estados(request):
    #pdb.set_trace()
    estados = Estado.objects.all().values()
    list_estado = list(estados)
    return JsonResponse(list_estado, safe=False)


def get_partidos(request):
    #pdb.set_trace()
    partidos = Partido.objects.all().values()
    list_partido = list(partidos)
    return JsonResponse(list_partido, safe=False)


def get_cargos(request):
    #pdb.set_trace()
    cargos = Cargo.objects.all().values()
    list_cargo = list(cargos)
    return JsonResponse(list_cargo, safe=False)


def busca_candidato(request):
    #pdb.set_trace()
    nome_candidato = request.GET.get("nome_candidato", None)
    candidatos = Candidato.objects.filter(nome=nome_candidato)
    list_candidato = list(candidatos.values())
    return JsonResponse(list_candidato, safe=False)
