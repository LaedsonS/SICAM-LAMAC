from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login_usuario'),
    path('cadastro/', views.cadastro, name='cadastro_usuario'),
    path('inicio/', views.inicio, name='inicio')
]