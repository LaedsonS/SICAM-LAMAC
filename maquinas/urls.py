from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/', views.solicitacao, name='criar_solicitacao'),
    path('adicionar/', views.adicionarMaquina, name='adicionar_maquina'),
    path('buscar/', views.buscar, name='buscar_maquina'),
    path('editar/', views.editarMaquina, name='editar_maquina'),
    path('registrarManutencao/', views.registrarManutencao, name='registrar_manutencao'),
    path('remover/', views.removerMaquina, name='remover_maquina')
]