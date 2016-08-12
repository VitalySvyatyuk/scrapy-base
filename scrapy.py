import requests
from bs4 import BeautifulSoup
import re

HEADERS = {'User-agent': 'Mozilla/5.0'}
currencies = open('currencies.txt').readlines()
for currency in currencies:
    url = 'http://www.investing.com/' + currency.rstrip()
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, "lxml")
    span = soup.find(id="last_last")
    print(span.contents[0])
