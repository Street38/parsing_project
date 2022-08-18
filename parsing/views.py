from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User


def home(request):
    return render(request, 'parsing/home.html')


def pageNotFound(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "parsing/signup.html"
    success_url = reverse_lazy("home")


def login(request):
    pass
