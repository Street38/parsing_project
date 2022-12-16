import os
import sys
import telebot
sys.path.append(os.path.join(sys.path[0], '../..'))
from parsing.tocken_bot import TOKEN
from parsing_project.wsgi import *
from parsing.models import PersonalAccount
from parsing.services.personal_account import update_peronalaccount, create_peronalaccount


bot = telebot.TeleBot(TOKEN)

'''Получает необходимые атрибуты объекта message и вызывает функцию создания либо изменения забиси в БД'''
@bot.message_handler(commands=['start'])
def start_bot(message):
    try:
        user_id = message.text.split(' ')[-1]
        chat_id = message.chat.id
        username = chat_id
        pers = PersonalAccount.objects.filter(user_id=user_id).first()
        if pers:
            update_peronalaccount(user_id, chat_id, username)
            bot.send_message(message.chat.id, 'Телеграмм успешно изменен')
        else:
            create_peronalaccount(user_id, chat_id, username)
            bot.send_message(message.chat.id, 'Телеграмм успешно сохранен')
    except Exception as e:
        bot.send_message(671618541, f'Шеф! Все пропало, опять чето сломалось. Скрипт = script_telegram_bot.py / Ошибка = {e}')


bot.polling()