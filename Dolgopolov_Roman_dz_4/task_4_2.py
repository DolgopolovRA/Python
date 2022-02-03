
from requests import get, utils
from decimal import Decimal

code = input('Введите код валюты: ')


def currency_rates(val_code):

    answer = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encode = utils.get_encoding_from_headers(answer.headers)
    content = answer.content.decode(encoding=encode).split('</Value>')
    ret = None
    if val_code.isalpha() and len(val_code) > 2:
        for i in content:
            if val_code.upper() in i:
                ret = Decimal(i[len(i) - 7:].replace(',', '.'))
                ret = ret.quantize(Decimal('1.00'))

    return ret


print(currency_rates(code))
