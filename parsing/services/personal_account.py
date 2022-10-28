from django.contrib.auth.models import User
from parsing.models import PersonalAccount

def create_peronalaccount(user_id, chat_id, username):
    '''Создает запись в таблице PersonalAccount'''
    user = User.objects.get(id=user_id)
    newrecord = PersonalAccount.objects.create(telegram_account=username, telegram_chat_id=chat_id)
    newrecord.user = user
    newrecord.save()
    return


def update_peronalaccount(user_id, chat_id, username):
    '''Обновляет запись в таблице PersonalAccount, в случае если телеграм изменился'''
    updaterecord = PersonalAccount.objects.get(user_id=user_id)
    updaterecord.telegram_account = username
    updaterecord.telegram_chat_id = chat_id
    updaterecord.save()
    return