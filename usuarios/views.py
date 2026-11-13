from django.shortcuts import render, redirect
from .forms import CadastroForms, LoginForms
from .models import Usuario

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForms()
        if form.is_valid():
            return redirect('login_usuario')
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
                senha = dados['senha']
            )
            return redirect('login_usuario')
    else:
        form = CadastroForms()
    return render(request, 'usuario/TelaCadastro.html', {'form':form})

def inicio(request):
    return render(request, 'base.html')
     