import telebot
from parsing.tocken_bot import TOKEN


bot = telebot.TeleBot(TOKEN)

def send_form_feedback(name, email, message):
    '''Отправляет сообщение с формы обратной связь'''
    bot.send_message(671618541, f'Имя - {name}, Почта - {email}, Текст сообщения - {message}')