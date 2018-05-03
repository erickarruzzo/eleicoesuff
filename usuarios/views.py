import code
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Usuario, Estado
from usuarios.forms import RegistrarUsuarioForm
from django.views.generic.base import View
from django.contrib.auth.hashers import PBKDF2PasswordHasher

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request, *args, **kwargs):
        estados = Estado.objects.all()
        return render(request, self.template_name, { 'estados' : estados })

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarUsuarioForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            hasher = PBKDF2PasswordHasher()
            dados_form = form.data
            estado = Estado.objects.get(id=dados_form['estado_register'])
            senha_hashed = hasher.encode(password=dados_form['senha_register1'],
                                         salt='salt',
                                         iterations=25000)
            #cria o usuario
            usuario = Usuario(cpf=dados_form['cpf_register'],
                                nome=dados_form['nome_register'],
                                email=dados_form['email_register'],
                                estado_id=estado,
                                senha=senha_hashed)
            #grava no banco
            usuario.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

def usuario(request, usuario_id):
	usuario = Usuario.objects.get(id=usuario_id)
	return render(request, 'usuario.html', { "usuario" : usuario })

def login(request):
	return render(request, 'login.html')
