import os
import sys
import telebot
sys.path.append(os.path.join(sys.path[0], '..'))
import parsing_project.wsgi
from get_price import get_price
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


def send_message_user(linkproduct, price, user_id, description):
    '''Отправляет сообщение пользователю'''
    user = PersonalAccount.objects.get(user_id=user_id)
    bot.send_message(user.telegram_chat_id, f'Цена на <b> {description} {price} р.</b> Перейти: {linkproduct}',
                     parse_mode="HTML")


daily_check_tracking()
