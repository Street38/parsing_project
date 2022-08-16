from django.shortcuts import render
from django.http import HttpResponseNotFound

def home(request):
    return render(request, 'parsing/home.html')

def pageNotFound(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')

def signup(request):
    pass

def login(request):
    pass