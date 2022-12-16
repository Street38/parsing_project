from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from parsing.validators.check_url import check_url


class TrackingModel(models.Model):
    description = models.CharField(max_length=200)
    linkproduct = models.URLField(max_length=250, validators=[check_url])
    price = models.IntegerField()
    datecomplite = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.description}, {self.price}"

    def get_url_tracking(self):
        url_link = reverse('update', args=[self.id])
        return url_link


class PersonalAccount(models.Model):
    telegram_account = models.CharField(max_length=50)
    telegram_chat_id = models.IntegerField(default=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Имя - {self.user} / Телеграм - {self.telegram_account}'


