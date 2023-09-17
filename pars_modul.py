from bs4 import BeautifulSoup as bs
import requests

def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    return soup

def pars_url_arists(soup): #извлекает ссылки на артистов с главной страницы
    result = {}
    html_list_info_artist = soup.find(
        'li', class_='t229__list_item').find_all('li', class_="t-menusub__list-item t-name t-name_xs")
    for html_artist in html_list_info_artist:
        name_artist = html_artist.text.strip()
        url_card_artist = html_artist.find(
            'a', class_="t-menusub__link-item t-name t-name_xs").get('href').strip()
        result[name_artist] = url_card_artist
    return result

def pars_url_product(dict_artist_url):
    for artist in dict_artist_url:
        url = f'https://glamgo.store{dict_artist_url[artist]}'
        soup = get_soup(url)
        
        d = soup.select(
            '#rec237654106 > div.t776 > div > div.js-store-grid-cont.t-store__grid-cont.t-container.t-store__grid-cont_mobile-grid > div:nth-child(1) > a > div.t-store__card__textwrapper > div.js-store-prod-name.js-product-name.t-store__card__title.t-typography__title.t-name.t-name_md')
        # print(d)
        for i in d:
            print(i)
