from django.shortcuts import render
from django.http import HttpResponse
from eleicoes2018.models import *

def index(request):
	usuarios = Usuario.objects.all()
	estados = Estado.objects.all()
	partidos = Partido.objects.all()
	cargos = Cargo.objects.all()
	candidatos = Candidato.objects.all()
	return render(request, 'index.html', { 'usuarios' : usuarios , 'estados' : estados , 'partidos' : partidos , 'cargos' : cargos , 'candidatos' : candidatos })
