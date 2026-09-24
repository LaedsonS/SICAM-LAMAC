from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionarMaquina, name='adicionar_maquina'),
    path('editar/', views.editarMaquina, name='editar_maquina'),
    path('remover/', views.removerMaquina, name='remover_maquina')
]