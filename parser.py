from bs4 import BeautifulSoup
import requests as req
import ipdb as pry
import sys

currency = input('Какой код валюты показать ? \n').upper().strip()
if len(currency) is 0:
    sys.exit('Sorry, currency code not input')

url = 'https://cbr.ru/currency_base/daily/'
page_source = req.get(url)
parse_page = BeautifulSoup(page_source.text, 'html.parser')

table_currencies = parse_page.find('table', {'class': 'data'})
tr = table_currencies.find_all('tr')

title_table = tr[0].text.replace('\n', ' ').split(' ')

hash_currency = {}
for i in tr[1:]:
    currency_title = i.text.replace('\n', ' ').strip().split(' ')
    currency_code = currency_title[1]
    float_value = float(currency_title[-1].replace(',', '.'))
    hash_currency[currency_code] = round(float_value, 2)
    # print(currency_code, round(float_value, 2))

print('Значение валюты', hash_currency[currency])
