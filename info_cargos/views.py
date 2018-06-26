from django.shortcuts import render
from eleicoes2018.models import *


def cargo(request, cargo_id):
    cargo = Cargo.objects.get(id=cargo_id)
    beneficios = Beneficio.objects.filter(cargo=cargo_id)
    return render(request, 'cargo.html', { "cargo" : cargo, 'beneficios' : beneficios })