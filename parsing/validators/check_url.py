from parsing.services.get_price import get_price
from django.core.exceptions import ValidationError


'''Валидация поля "linkproduct", на корректность ввода ссылки на имеющийся товар на WB'''
def check_url(value):
    price = get_price(value)
    if price and 'wildberries.ru' in value:
        return value
    else:
        raise ValidationError('Ссылка указана не верно')
