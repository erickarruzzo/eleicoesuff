from django.db import models
from django.contrib.auth.models import User
#import datetime

import math

class Estado(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=2, null=False)
    total_eleitores = models.IntegerField(null=False, default=5000000)

    def getNumDepFederal(self):
        n = math.ceil(self.total_eleitores/370000)
        if n < 8:
            return 8
        elif n > 70:
            return 70
        return n  

    def getNumDepEstadual(self):
        n = self.getNumDepFederal()
        if n >= 12:
            return n+24            
        return n*3


class LocalVotacao(models.Model):
    zona = models.IntegerField(null=False)
    secao = models.IntegerField(null=False)
    local = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    cpf = models.CharField(max_length=11, null=False)
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    senha = models.CharField(max_length=255, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    local_votacao = models.ForeignKey(LocalVotacao, on_delete=models.CASCADE, null=True)


class Cargo(models.Model):
    nome = models.CharField(max_length=255, null=False)


class Partido(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=6, null=False)


class Candidato(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    total_votos = models.IntegerField(null=False, default=0)



class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)


class Info(models.Model):
    texto = models.CharField(max_length=255, null=False)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)


class Noticia(models.Model):
    titulo = models.CharField(max_length=255, null=False)
    link = models.CharField(max_length=255, null=False)
    data = models.DateTimeField()
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True)



class InfoCargo(models.Model):
    texto = models.CharField(max_length=500, null=False)
    salario = models.FloatField(null=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)