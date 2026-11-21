from django.db import models

# Create your models here.
class Solicitacao(models.Model):
    nome_proprietario = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    problema = models.CharField()

    def __str__(self):
        return self.modelo

class Maquina(models.Model):
    nome_proprietario = models.CharField(max_length=100)
    modelo = models.CharField(max_length=20)
    modelo_processador = models.CharField()
    defeito = models.CharField()

    def __str__(self):
        return self.modelo
    
class Manutencao(models.Model):
    tecnico = models.CharField(max_length=100)
    maquina = models.CharField()
    procedimento = models.CharField(max_length=200)
    data = models.DateField()

    def __str__(self):
        return self.modelo