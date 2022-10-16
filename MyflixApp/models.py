from django.db import models
import uuid






# Create your models here.

class Myflix(models.Model):
    uuid = models.UUIDField( default=uuid.uuid4)
    nome_filme = models.CharField(max_length=200)
    sinospse = models.TextField(max_length=500)
    elenco = models.TextField(max_length=200)
    tempo_filme = models.IntegerField(null=True)
    lancamento = models.CharField(max_length=20,null=True)
    classificacao = models.CharField(max_length=20, null=True)
    id_video = models.CharField(max_length=20,null=True)
    capa_filme = models.ImageField(upload_to='banners',null=True)
    categoria = models.ForeignKey('Genero',on_delete=models.CASCADE, null=True)
    publicada = models.BooleanField(default=False)


    def __str__(self):
        return self.nome_filme

class Genero(models.Model):
    generos_filmes = models.CharField(max_length=10, null=True)

    def __str__(self):
        return  self.generos_filmes





