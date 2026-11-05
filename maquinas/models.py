from django.db import models

# Create your models here.
class Maquina(models.Model):
    nome_proprietario = models.CharField(max_length=100)
    modelo = models.CharField(max_length=20)
    modelo_processador = models.CharField()
    problema = models.CharField()

    def __str__(self):
        return self.modelo

class Manutencao(models.Model):
    tecnico = models.CharField(max_length=100)
    procedimento = models.CharField(max_length=200)
    data = models.DateField()
    problema = models.CharField()

    def __str__(self):
        return self.modelo