import os
import sys
import telebot
from pprint import pprint
sys.path.append(os.path.join(sys.path[0], '..'))
pprint(sys.path)
import parsing_project.wsgi
from parsing.services.get_price_stocks import get_price
from parsing.services.get_price_stocks import get_stocks
from parsing.models import TrackingModel, PersonalAccount
from parsing.tocken_bot import TOKEN

bot = telebot.TeleBot(TOKEN)


def daily_check_tracking():
    '''Прверка всех активных отслеживаний из таблицы TrackingModel, на условие достижения цены'''
    trackings = TrackingModel.objects.filter(datecomplite__isnull=True)
    for tracking in trackings:
        linkproduct = tracking.linkproduct
        price, data = get_price(linkproduct)
        stocks = get_stocks(data)
        if stocks and price <= tracking.price:
            send_message_user(linkproduct, price, tracking.user_id, tracking.description)


def send_message_user(linkproduct, price, user_id, description):
    '''Отправляет сообщение пользователю'''
    user = PersonalAccount.objects.get(user_id=user_id)
    bot.send_message(user.telegram_chat_id, f'Цена на <b> {description} {price} р.</b> Перейти: {linkproduct}',
                     parse_mode="HTML")


'''Запуск функции при выполнении скрипта'''
daily_check_tracking()
