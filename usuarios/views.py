import code
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eleicoes2018.models import Usuario, Estado
from usuarios.forms import RegistrarUsuarioForm
from django.views.generic.base import View

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        #preenche o form
        form = RegistrarUsuarioForm(request.POST)
        #verifica se eh valido
        if form.is_valid():
            dados_form = form.data
            estado = Estado.objects.get(id=dados_form['estado_register'])

            #cria o usuario
            usuario = Usuario(cpf=dados_form['cpf_register'],
                                nome=dados_form['nome_register'],
                                email=dados_form['email_register'],
                                estado_id=estado,
                                senha=dados_form['senha_register1'])
            #grava no banco
            usuario.save()

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

def usuario(request, usuario_id):
	usuario = Usuario.objects.get(id=usuario_id)
	return render(request, 'usuario.html', { "usuario" : usuario })

def login(request):
	return render(request, 'login.html')
