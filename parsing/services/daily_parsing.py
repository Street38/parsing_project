import os
import sys
import telebot
import requests
sys.path.append(os.path.join(sys.path[0], '../..'))
from parsing_project.wsgi import *
from parsing.models import TrackingModel, PersonalAccount
from parsing.tocken_bot import TOKEN
from django.db.models import Q

bot = telebot.TeleBot(TOKEN)


def daily_check_tracking():
    '''Прверка всех активных отслеживаний из таблицы TrackingModel, на условие достижения цены'''
    trackings = TrackingModel.objects.filter(Q(datecomplite__isnull=True) & Q(user_id=1))
    for tracking in trackings:
        linkproduct = tracking.linkproduct
        price = get_price(linkproduct)
        if price <= tracking.price:
            send_message_user(linkproduct, price, tracking.user_id)


def get_price(linkproduct):
    link_card = get_link_card(linkproduct)
    response = requests.get(link_card)
    data = response.json()
    price = int(data['data']['products'][0]['salePriceU'] / 100)
    return price


def get_link_card(linkproduct):
    id = linkproduct.split('/')[-2]
    link_card = f"https://card.wb.ru/cards/" \
                f"detail?spp=0&regions=64,58,83,4,38,80,33,70,82,86,30,69,22,66,31,40,1," \
                f"48&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,21,16&" \
                f"dest=-1221148,-145454,-1430613,-5827642&nm={id}"
    return link_card


def send_message_user(linkproduct, price, user_id):
    '''Отправляет сообщение пользователю'''
    user = PersonalAccount.objects.get(user_id=user_id)
    bot.send_message(user.telegram_chat_id, f'Налетай, успевай, покупай, цена {price} р. Ссылька {linkproduct}')
