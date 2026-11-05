from django.shortcuts import render, redirect
from .forms import CadastroMaquinaForm, AtulizacaoMaquinaForm, RegistrarManutencao, CadastroSolicitacao

# Create your views here.
def solicitacao(request):
    if request.method == 'POST':
        form = CadastroSolicitacao(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = CadastroSolicitacao()
    return render(request, 'maquina/Solicitacao.html', {'form':form})
    
def adicionarMaquina(request):
    if request.method == 'POST':
        form = CadastroMaquinaForm(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = CadastroMaquinaForm()
    return render(request, 'maquina/TelaAdicionarMaquina.html', {'form':form})
    

def editarMaquina(request):
    if request.method == 'POST':
        form = AtulizacaoMaquinaForm(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = AtulizacaoMaquinaForm()
    return render(request, 'maquina/TelaAtualizacao.html', {'form':form})

def removerMaquina(request):
    return render(request, 'maquina/TelaRemoverMaquina.html')

def registrarManutencao(request):
    if request.method == 'POST':
        form = RegistrarManutencao(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = RegistrarManutencao()
    return render(request, 'maquina/RegistrarManutencao.html',{'form':form})

def buscar(request):
    return render(request, 'maquina/BuscarMaquina.html')