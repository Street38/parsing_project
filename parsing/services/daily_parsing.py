import os
import sys
import telebot
import requests
sys.path.append(os.path.join(sys.path[0], '..'))
import parsing_project.wsgi
from parsing.models import TrackingModel, PersonalAccount
from parsing.tocken_bot import TOKEN

bot = telebot.TeleBot(TOKEN)


def daily_check_tracking():
    '''Прверка всех активных отслеживаний из таблицы TrackingModel, на условие достижения цены'''
    trackings = TrackingModel.objects.filter(datecomplite__isnull=True)
    for tracking in trackings:
        linkproduct = tracking.linkproduct
        price = get_price(linkproduct)
        if price <= tracking.price:
            send_message_user(linkproduct, price, tracking.user_id, tracking.description)


def get_price(linkproduct):
    link_card = get_link_card(linkproduct)
    response = requests.get(link_card)
    data = response.json()
    try:
        price = int(data['data']['products'][0]['salePriceU'] / 100)
        return price
    except:
        return None


def get_link_card(linkproduct):
    id = linkproduct.split('/')[-2]
    '''Не авторизованный запрос'''
    link_card = f"https://card.wb.ru/cards/detail?spp=0&regions=80,64,58,83,4,38,33,70,82,69," \
                f"68,86,30,40,48,1,22,66,31&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&" \
                f"locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,21,16&dest=-1221148," \
                f"-145454,-1430613,-5827642&nm={id}"
    '''Авторизованный запрос'''
    # link_card = f"https://card.wb.ru/cards/detail?spp=28&regions=80,64,58,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66," \
    #             f"31&pricemarginCoeff=1.0&reg=1&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,12,7,3,6,21," \
    #             f"16&sppFixGeo=4&dest=-1221148,-145454,-1430613,-5827226&nm={id}"
    return link_card


def send_message_user(linkproduct, price, user_id, description):
    '''Отправляет сообщение пользователю'''
    user = PersonalAccount.objects.get(user_id=user_id)
    bot.send_message(user.telegram_chat_id, f'Цена на <b> {description} {price} р.</b> Перейти: {linkproduct}',
                     parse_mode="HTML")


daily_check_tracking()
