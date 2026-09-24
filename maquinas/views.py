from django.shortcuts import render

# Create your views here.
def adicionarMaquina(request):
    return render(request, 'maquina/TelaAdicionarMaquina.html')

def editarMaquina(request):
    return render(request, 'maquina/TelaAtualizacao.html')

def removerMaquina(request):
    return render(request, 'maquina/TelaRemoverMaquina.html')