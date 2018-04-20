from django.db import models

class Estado(models.Model):
	nome = models.CharField(max_length=255, null=False)
	sigla = models.CharField(max_length=2, null=False)

class Usuario(models.Model):
	cpf = models.CharField(max_length=11, null=False)
	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	senha = models.CharField(max_length=255, null=False)
	estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Cargo(models.Model):
	nome = models.CharField(max_length=255, null=False)	

class Partido(models.Model):
	nome = models.CharField(max_length=255, null=False)
	sigla = models.CharField(max_length=2, null=False)
		

class Candidato(models.Model):
	nome = models.CharField(max_length=255, null=False)
	cargo_id = models.ForeignKey(Cargo, on_delete=models.CASCADE)
	partido_id = models.ForeignKey(Partido, on_delete=models.CASCADE)
	estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE)	

class Voto(models.Model):
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	cargo_id = models.ForeignKey(Cargo, on_delete=models.CASCADE)
	candidato_id = models.ForeignKey(Candidato, on_delete=models.CASCADE)