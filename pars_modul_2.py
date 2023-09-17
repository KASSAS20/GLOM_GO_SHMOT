import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://glamgo.store/gonefludd/tproduct/237654106-747909980751-futbolka-digital-fantazy'

def chars_item_to_url():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find_all('div', class_ = 't-store__prod-popup__title-wrapper')
    price = soup.find_all('div', class_ = 'js-product-price js-store-prod-price-val t-store__prod-popup__price-value')
    chars = soup.find_all('p', class_ = 'js-store-prod-charcs')

    for i in name:
        name = i.text.strip()

    for i in price:
        price = i.text.strip()

    types = chars[0].text
    color = chars[1].text
    structure = chars[2].text
    application_chest = chars[3].text
    application_back = chars[4].text
        
    chars_name = {
        "name": name,
        'price': price,
        'types' : types,
        'color' : color,
        'structure' : structure,
        'application_chest' : application_chest,
        'application_back' : application_back,
    }
