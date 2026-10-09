from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField()
    matricula = models.CharField(max_length=14, unique=True)
    senha = models.CharField()

    def __str__(self):
        return self.nome
