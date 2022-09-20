from django.db import models


# Create your models here.

class Myflix(models.Model):
    nome_filme = models.CharField(max_length=200)
    elenco = models.TextField(max_length=100)
    sinospse = models.TextField(max_length=200)
    tempo_filme = models.IntegerField(null=True)
    capa_filme = models.ImageField(upload_to='banners',null=True)
    filme = models.FileField(upload_to="filme")

    def __str__(self):
        return self.nome_filme