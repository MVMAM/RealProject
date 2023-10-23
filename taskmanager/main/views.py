# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TaskForm, UserForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title' : 'Главная страница сайта', 'tasks' : tasks})


def about(request):
    return render(request, 'main/about.html')


# @login_required
def creator(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была неверной"

    form = TaskForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/creator.html', context)


def info(request):
    return render(request, 'main/info.html')


def registrator(request):
    return render(request, 'main/registrate.html')


def log_in(request):
    return render(request, 'main/log_in.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('home')
        else:
            messages.error(request,
                           "Please correct the errors below.")

    context = {'form': UserForm()}
    return render(request, 'create_user.html', context)