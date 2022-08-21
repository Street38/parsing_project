from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'parsing/home.html')


def pageNotFound(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "parsing/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tracking')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'parsing/login.html'

class LogoutView(LogoutView):
     template_name = "registration/logged_out.html"

@login_required
def tracking(request):
    return render(request, 'parsing/tracking.html')