from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:uuid>/', views.detail,name='movie-detail')
]