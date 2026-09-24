from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'usuario/TelaLogin.html')

def cadastro(request):
    return render(request, 'usuario/TelaCadastro.html')

def inicio(request):
    return render(request, 'usuario/TelaInicial.html')