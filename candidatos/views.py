from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from eleicoes2018.models import *
from candidatos.forms import RegistrarCandidatoForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.base import View
import pymysql.cursors
import pdb

class RegistrarCandidatoView(View):

    template_name = 'registrar_candidato.html'

    def get(self, request, *args, **kwargs):
        estados = Estado.objects.all()
        partidos = Partido.objects.all()
        cargos = Cargo.objects.all()
        return render(request, self.template_name, { 'estados' : estados , 'partidos' : partidos , 'cargos' : cargos })

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarCandidatoForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data

            partido = Partido.objects.get(id=dados_form['partido_register'])
            estado = Estado.objects.get(id=dados_form['estado_register'])
            cargo = Cargo.objects.get(id=dados_form['cargo_register'])

            #cria o candidato
            candidato = Candidato(nome=dados_form['nome_register'],
                                partido=partido,
                                estado=estado,
                                cargo=cargo)
            #grava no banco
            candidato.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

def candidato(request, candidato_id):
    candidato = Candidato.objects.get(id=candidato_id)
    infos = Info.objects.filter(candidato=candidato_id)
    return render(request, 'candidato.html', { "candidato" : candidato, 'infos' : infos })


def candidatos(request):
    candidatos_lista = Candidato.objects.all()
    paginator = Paginator(candidatos_lista, 10) # Mostra 10 candidatos por página
    page = request.GET.get('pagina')
    cargos = Cargo.objects.all().order_by('nome')
    candidatos = paginator.get_page(page)
    partidos = Partido.objects.all().order_by('nome')
    estados = Estado.objects.all().order_by('nome')
    return render(request, 'candidatos.html', { "candidatos" : candidatos, "cargos" : cargos, "estados" : estados, "partidos" : partidos })

def get_candidatos_com_filtro(request):
    nome = request.GET.get("nome", None)
    cargo_id = request.GET.get("cargo", None)
    estado_id = request.GET.get("estado", None)
    partido_id = request.GET.get("partido", None)

    #pdb.set_trace()

    # Conectando-se ao banco de dados
    connection = pymysql.connect(host='localhost',
                            user='erick',
                            password='123',
                            db='eleicoes',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT candidato.id, candidato.nome candidato, partido.sigla partido, estado.sigla estado, cargo.nome cargo FROM `eleicoes2018_candidato` candidato left join `eleicoes2018_partido` partido on candidato.partido_id = partido.id left join `eleicoes2018_estado` estado on candidato.estado_id = estado.id left join `eleicoes2018_cargo` cargo on candidato.cargo_id = cargo.id WHERE 1=1 "
            
            if nome != '': 
                sql += "and candidato.nome like '%" + nome + "%' "
            
            if cargo_id != '':
                sql += "and candidato.cargo_id =" + cargo_id + " "

            if estado_id != '':
                sql += "and candidato.estado_id =" + estado_id + " "

            if partido_id != '':
                sql += "and candidato.partido_id =" + partido_id + " "

            cursor.execute(sql)
            result = cursor.fetchall()

            #pdb.set_trace()

            return JsonResponse(result, safe=False)
    finally:
        connection.close()
