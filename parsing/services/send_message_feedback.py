import telebot
from parsing.tocken_bot import TOKEN


bot = telebot.TeleBot(TOKEN)

def send_form_feedback(feedback, username):
    '''Отправляет сообщение в телеграм с формы обратной связь'''
    list_values = [i for i in (feedback).values()]
    list_values.append(username)
    bot.send_message(671618541, f'Имя - {list_values[1]}\nНомер телефона - {list_values[2]}\nПочта - \n'
                                f'Текст сообщения - {list_values[3]}\nИмя в аккаунте - {list_values[-1]}')