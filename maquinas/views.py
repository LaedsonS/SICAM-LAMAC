from django.shortcuts import render, redirect
from .forms import CadastroMaquinaForm, EdicaoMaquinaForm, RegistrarManutencao, CadastroSolicitacao
from .models import Maquina, Solicitacao, Manutencao

# Create your views here.
def solicitacao(request):
    if request.method == 'POST':
        form = CadastroSolicitacao(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            Solicitacao.objects.create(
                nome_proprietario = dados['nome_proprietario'],
                modelo_computador = dados['modelo_computador'],
                problema = dados['problema']
            )
            return redirect('inicio')
    else:
        form = CadastroSolicitacao()
    return render(request, 'maquina/Solicitacao.html', {'form':form})
    
def adicionarMaquina(request):
    if request.method == 'POST':
        form = CadastroMaquinaForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            Maquina.objects.create(
                nome_proprietario = dados['nome_proprietario'],
                modelo_computador = dados['modelo_computador'],
                modelo_processador = dados['modelo_processador'],
                defeito = dados['defeito']
            )
            return redirect('inicio')
    else:
        form = CadastroMaquinaForm()
    return render(request, 'maquina/TelaAdicionarMaquina.html', {'form':form})

def registrarManutencao(request):
    if request.method == 'POST':
        form = RegistrarManutencao(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            Manutencao.objects.create(
                tecnico = dados['tecnico'],
                maquina = dados['maquina'],
                procedimento = dados['procedimento'],
                data = dados['data']
            )
            return redirect('inicio')
    else:
        form = RegistrarManutencao()
    return render(request, 'maquina/RegistrarManutencao.html',{'form':form})

def editarMaquina(request):
    if request.method == 'POST':
        form = EdicaoMaquinaForm(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = EdicaoMaquinaForm()
    return render(request, 'maquina/EdicaoMaquina.html', {'form':form})

def removerMaquina(request):
    return render(request, 'maquina/TelaRemoverMaquina.html')

def buscar(request):
    return render(request, 'maquina/BuscarMaquina.html')