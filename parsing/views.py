from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm


def home(request):
    return render(request, 'parsing/home.html')


def pageNotFound(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "parsing/signup.html"
    success_url = reverse_lazy("home")


def login(request):
    pass
