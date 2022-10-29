from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import SignupForm, LoginForm, CreateTrackingForm, UpdateTrackingForm, ArchiveTrackingForm, PersonalForms
from django.contrib.auth.views import LoginView, LogoutView
from .models import TrackingModel, PersonalAccount
from django.utils import timezone
from django.db.models import Q


def home(request):
    return render(request, 'parsing/home.html')


def pageNotFound(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'parsing/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('current')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'parsing/login.html'


class LogoutView(LogoutView):
    template_name = "registration/logged_out.html"


class CompliteListView(ListView):
    template_name = 'parsing/complite.html'
    model = TrackingModel
    context_object_name = 'tracking'

    def get_queryset(self):
        return super().get_queryset().filter(Q(user_id=self.request.user) & Q(datecomplite__isnull=False))


class ArchiveTrackingView(UpdateView):
    form_class = ArchiveTrackingForm
    template_name = 'parsing/archive.html'
    model = TrackingModel
    context_object_name = 'tracking'


class CurrentListView(ListView):
    template_name = 'parsing/current.html'
    model = TrackingModel
    context_object_name = 'tracking'

    def get_queryset(self):
        return super().get_queryset().filter(Q(user_id=self.request.user) & Q(datecomplite=None))


class UpdateTrackingView(UpdateView):
    form_class = UpdateTrackingForm
    model = TrackingModel
    template_name = "parsing/update.html"
    success_url = reverse_lazy("current")

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = context['trackingmodel'].linkproduct
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get("complete"):
            tracking = self.get_object()
            tracking.datecomplite = timezone.now()
            tracking.save()
            return super().post(self, request)
        else:
            return super().post(self, request)


class CreateTrackingView(CreateView):
    form_class = CreateTrackingForm
    template_name = "parsing/create.html"
    success_url = reverse_lazy("current")

    def form_valid(self, form):
        newlink = form.save(commit=False)
        newlink.user = self.request.user
        newlink.save()
        return redirect("current")


# class PersonalAccountView(DetailView):
#     model = PersonalAccount
#     template_name = 'parsing/personal.html'
#     context_object_name = 'form'
#
#     def get_object(self, queryset=None):
#         return super().get_queryset().filter(user_id=self.kwargs['pk']).first()


class PersonalAccountView(UpdateView):
    model = PersonalAccount
    form_class = PersonalForms
    template_name = 'parsing/personal.html'

    def get_object(self, queryset=None):
        return super().get_queryset().filter(user_id=self.kwargs['pk']).first()

    def get_context_data(self, **kwargs):
        '''Передаем username в поле name, формы PersonalForms '''
        context = super().get_context_data(**kwargs)
        context['form'].initial['name'] = self.request.user.username
        return context
