from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import *
from django.views.generic.base import View
from django.http import JsonResponse
import pdb

def resultado(request):
    estados = Estado.objects.all()
    cargos = Cargo.objects.all()
    return render(request, 'resultado.html', { "estados" : estados, 'cargos' : cargos })