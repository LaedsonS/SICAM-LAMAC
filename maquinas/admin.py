from django.contrib import admin
from .models import Maquina, Solicitacao, Manutencao
# Register your models here.
admin.site.register(Maquina)
admin.site.register(Solicitacao)
admin.site.register(Manutencao)