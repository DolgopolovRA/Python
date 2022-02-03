from utils import currency_rates
from sys import argv


if len(argv) == 1:
    code = input('Введите код валюты: ')
else:
    code = argv[1]

print(currency_rates(code))
