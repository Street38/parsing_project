import requests

"""Используется в models.py как валидатор поля linkproduct и в daily_parsing.py"""
def get_price(linkproduct):
    link_card = get_link_card(linkproduct)
    response = requests.get(link_card)
    data = response.json()
    try:
        price = int(data['data']['products'][0]['salePriceU'] / 100)
        return price, data
    except:
        return None


def get_stocks(data):
    try:
        stocks = data['data']['products'][0]['sizes'][0]['stocks']
        return stocks
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
