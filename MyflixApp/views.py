from django.shortcuts import render
from .models import Myflix, Genero

def index(request):
    video = Myflix.objects.all()
    genero = Genero.objects.all()



    return render(request,'index.html',{"video":video, "genero":genero })

def filmes(request):

    return render(request,'filmes.html')

