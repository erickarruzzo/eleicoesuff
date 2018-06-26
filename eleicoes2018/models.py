from django.db import models
from django.contrib.auth.models import User
#import datetime


class Estado(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=2, null=False)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    cpf = models.CharField(max_length=11, null=False)
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    senha = models.CharField(max_length=255, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Cargo(models.Model):
    nome = models.CharField(max_length=255, null=False)
    salario = models.FloatField(null=False)
    descricao = models.CharField(max_length=255, null=False)


class Partido(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=6, null=False)


class Candidato(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    votos_recebidos = models.IntegerField(default=0)


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

# class LocalVotacao(models.Model):
#	titulo = models.CharField(max_length=255, null=False)
#	link = models.CharField(max_length=255, null=False)

class Beneficio(models.Model):
	nome = models.CharField(max_length=255, null=False)
	descricao = models.CharField(max_length=255, null=False)

class CargoBeneficio(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
