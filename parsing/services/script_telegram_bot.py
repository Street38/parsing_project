import telebot
from config.wsgi import *
from parsing.tocken_bot import TOKEN
from parsing.models import PersonalAccount
from parsing.services.personal_account import update_peronalaccount, create_peronalaccount

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    '''Получает необходимые атрибуты объекта message и вызывает функцию создания либо изменения забиси в БД'''
    user_id = message.text.split(' ')[-1]
    chat_id = message.chat.id
    username = '@' + message.from_user.username
    pers = PersonalAccount.objects.filter(user_id=user_id).first()
    if pers:
        update_peronalaccount(user_id, chat_id, username)
        bot.send_message(message.chat.id, 'Телеграмм успешно изменен')
    else:
        create_peronalaccount(user_id, chat_id, username)
        bot.send_message(message.chat.id, 'Телеграмм успешно подключен')


def send_message_user(linkproduct, price, user_id):
    '''Отправляет сообщение пользователю'''
    user = PersonalAccount.objects.get(user_id=user_id)
    bot.send_message(user.telegram_chat_id, f'Цена снизилась, составляет {price} р, можно брать')


bot.polling()
