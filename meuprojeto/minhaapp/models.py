from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome