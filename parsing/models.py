import requests
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
# from parsing.services.daily_parsing import get_price
# import parsing.validators.chek_valid_url


def check_url(value):
    from parsing.services.daily_parsing import get_price
    price = get_price(value)
    if price:
        return value
    else:
        raise ValidationError('Ссылка указана не верно')
#
# def get_price(linkproduct):
#     link_card = get_link_card(linkproduct)
#     response = requests.get(link_card)
#     data = response.json()
#     try:
#         price = int(data['data']['products'][0]['salePriceU'] / 100)
#         return price
#     except:
#         return None
#
# def get_link_card(linkproduct):
#     try:
#         id = linkproduct.split('/')[-2]
#         '''Не авторизованный запрос'''
#         link_card = f"https://card.wb.ru/cards/detail?spp=0&regions=80,64,58,83,4,38,33,70,82,69," \
#                     f"68,86,30,40,48,1,22,66,31&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&" \
#                     f"locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,21,16&dest=-1221148," \
#                     f"-145454,-1430613,-5827642&nm={id}"
#         '''Авторизованный запрос'''
#     # link_card = f"https://card.wb.ru/cards/detail?spp=28&regions=80,64,58,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66," \
#     #             f"31&pricemarginCoeff=1.0&reg=1&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,21," \
#     #             f"16&sppFixGeo=4&dest=-1221148,-145454,-1430613,-5827226&nm={id}"
#         return link_card
#     except IndexError:
#         return None


class TrackingModel(models.Model):
    description = models.CharField(max_length=200)
    linkproduct = models.URLField(max_length=250, validators=[check_url])
    price = models.IntegerField()
    datecomplite = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    def get_url_tracking(self):
        url_link = reverse('update', args=[self.id])
        return url_link


class PersonalAccount(models.Model):
    telegram_account = models.CharField(max_length=50)
    telegram_chat_id = models.IntegerField(default=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
