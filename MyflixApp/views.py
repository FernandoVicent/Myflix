from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Myflix, Genero



def index(request):
    video = Myflix.objects.filter(publicada=True)
    generos = Genero.objects.all()


    return render(request,'index.html',{"video":video, "generos":generos})

def detail(request,uuid):
    lookup_field = "name"

    movie = Myflix.objects.get(uuid=uuid)
    video = Myflix.objects.filter(publicada=True)
    generos = Genero.objects.all()
    context = {
        'video':video,
        'genero': generos,
        'post':movie
    }
    return render(request,'filmes.html',context)
