from django.shortcuts import render
from django.http import HttpResponse
from eleicoes2018.models import Usuario, Estado

def index(request):
	usuarios = Usuario.objects.all()
	estados = Estado.objects.all()
	return render(request, 'index.html', { 'usuarios' : usuarios , 'estados' : estados })


def usuario(request, usuario_id):
	usuario = Usuario.objects.get(id=usuario_id)
	return render(request, 'usuario.html', { "usuario" : usuario })

def login(request):
	return render(request, 'login.html')