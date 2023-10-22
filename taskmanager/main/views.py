from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


def about(request):
    return render(request, 'main/about.html')

def     path('about', views.about, name="about"),
(request):
    return render(request, 'main/creator.html')