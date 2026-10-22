from django.shortcuts import render, redirect
from .forms import CadastroMaquinaForm, AtulizacaoMaquinaForm

# Create your views here.
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

def buscar(request):
    return render(request, 'maquina/BuscarMaquina.html')