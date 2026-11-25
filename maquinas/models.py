from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Solicitacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modelo_computador = models.CharField(max_length=20)
    problema = models.CharField()
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo_computador

class Maquina(models.Model):
    nome_proprietario = models.CharField(max_length=100)
    modelo_computador = models.CharField(max_length=20)
    modelo_processador = models.CharField()
    defeito = models.CharField()

    def __str__(self):
        return self.modelo_computador
    
class Manutencao(models.Model):
    tecnico = models.CharField(max_length=100)
    maquina = models.CharField()
    procedimento = models.CharField(max_length=200)
    data = models.DateField()

    def __str__(self):
        return self.tecnico