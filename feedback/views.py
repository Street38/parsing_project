from django.shortcuts import render, HttpResponse
from .forms import FeedbackForms
from django.views.generic import View, CreateView
from .models import FeedbackModel
from django.urls import reverse_lazy
from parsing.services.send_message_feedback import send_form_feedback
from django.contrib.auth.models import User
from django.utils import timezone


class FeedbackView(View):
    def get(self, request):
        form = FeedbackForms()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForms(request.POST)
        if form.is_valid():
            if self.request.user.username: # Проверка, залогинен или нет, если да, то к сообщению привязывается пользователь из модели User.
                newfeedback = form.save(commit=False)
                newfeedback.user = User.objects.get(username=self.request.user.username)
                newfeedback.date = timezone.now()
                newfeedback.save()
                send_form_feedback(self.request.POST, self.request.user.username)
                return render(request, 'feedback/done.html')
            else:
                newfeedback = form.save(commit=False)
                newfeedback.date = timezone.now()
                newfeedback.save()
                send_form_feedback(self.request.POST, self.request.user.username)
                return render(request, 'feedback/done.html')
        else:
            return render(request, 'feedback/feedback.html', context={'form': form})



def done(request):
    return render(request, 'feedback/done.html')

# class FeedbackView(CreateView):
#     model = FeedbackModel
#     form_class = FeedbackForms
#     template_name = 'feedback/feedback.html'
#     success_url = 'done'
