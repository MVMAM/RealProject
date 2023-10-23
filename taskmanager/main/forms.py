from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description")
        widgets = {
            "title" : TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Введите название"
            }),
            "description" : Textarea(attrs={
                "class" : "form-control",
                "placeholder" : "Введите текст (описание)"
            })
        }

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             help_text="We never share your email with anyone else.")

    class Meta:
        model = User
        fields = ('username', 'email',
                  'password1', 'password2')