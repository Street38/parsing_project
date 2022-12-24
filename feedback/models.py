from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone


class FeedbackModel(models.Model):
    name = models.CharField(max_length=15)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"Имя - {self.name} / Телефон - {self.phone_number} / Сообщение - {self.message} / Дата - {self.date}"
