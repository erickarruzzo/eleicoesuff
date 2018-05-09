from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from eleicoes2018.models import *
from django.http import JsonResponse
import json
import pdb

def boca_de_urna(request):
    usuarios = Usuario.objects.all()
    estados = Estado.objects.all()
    partidos = Partido.objects.all()
    cargos = Cargo.objects.all()
    candidatos = Candidato.objects.all()
    presidentes = Candidato.objects.filter(cargo_id=1) #presidente
    governadores = Candidato.objects.filter(cargo_id=2) #governador
    senadores = Candidato.objects.filter(cargo_id=3) #senador
    federais = Candidato.objects.filter(cargo_id=4) #deputado federal
    estaduais = Candidato.objects.filter(cargo_id=5) #deputado estadual

    return render(request, 'boca_de_urna.html', { 'usuarios':usuarios, 'estados':estados, 'partidos':partidos,
    'cargos':cargos, 'candidatos':candidatos, 'presidentes':presidentes, 'governadores':governadores,
    'senadores':senadores, 'federais':federais, 'estaduais':estaduais})

def contador_votos(request, candidatos, cargo, estado):

    if cargo.id != 1:
        votos = Voto.objects.filter(candidato_id__cargo_id_id=cargo.id, candidato_id__estado_id_id=estado.id)
    else:
        votos = Voto.objects.filter(candidato_id__cargo_id_id=cargo.id)

    json_string = json.dumps(votos)

    return JsonResponse(json_string)
