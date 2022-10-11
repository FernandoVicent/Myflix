from django.shortcuts import render
from .models import Myflix, Genero



def index(request):
    video = Myflix.objects.filter(publicada=True)
    generos = Genero.objects.all()


    return render(request,'index.html',{"video":video, "generos":generos})


def filmes(request):


    return render(request,'filmes.html')

