from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


def about(request):
    return render(request, 'main/about.html')

def creator(request):
    form = TaskForm()
    context = {
        'form' : form
    }
    return render(request, 'main/creator.html', context)