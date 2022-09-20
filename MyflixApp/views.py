from django.shortcuts import render
from .models import Myflix

def index(request):
    video = Myflix.objects.all()

    return render(request,'index.html',{"video":video})

def filmes(request):

    return render(request,'filmes.html')

