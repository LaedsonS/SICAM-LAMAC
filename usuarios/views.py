from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import CadastroForms, LoginForms
from .models import Usuario
from maquinas.models import Solicitacao

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            request.session['usuario_id'] = form.cleaned_data['usuario']. id
            return redirect('inicio')
    else:
        form = LoginForms()

    return render(request, 'usuario/TelaLogin.html', {'form':form})

def cadastro(request):
    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            Usuario.objects.create(
                nome = dados['nome'],
                matricula = dados['matricula'],
                email = dados['email'],
                senha = make_password(dados['senha'])
            )
            return redirect('login_usuario')
    else:
        form = CadastroForms()
    return render(request, 'usuario/TelaCadastro.html', {'form':form})     

def inicio(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login_usuario')

    usuario = Usuario.objects.get(id=usuario_id)
    solicitacoes = (Solicitacao.objects.filter(usuario=usuario)).order_by('data')

    return render(request, 'usuario/TelaInicial.html', {'usuario': usuario,'solicitacoes': solicitacoes,})