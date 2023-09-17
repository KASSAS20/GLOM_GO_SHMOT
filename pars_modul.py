from bs4 import BeautifulSoup as bs
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_soup(url):  # получение html страницы через requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    return soup


def get_soup_from_selenium(url):  # получение html страницы через селениум
    user_agent = "'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'"
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    option.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Firefox(options=option)
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    wait.until(EC.presence_of_element_located(('css selector', '#nav238128853 > div.t830__panel.t830__panel_bg.t830__panel_hover.t830__panel_open > div.t830__menu__content > div.t830__burger.t830__burger_mobile')))
    html = driver.page_source
    soup = bs(html, 'lxml')
    driver.quit()
    return soup


def pars_url_arists(soup):  # извлекает ссылки на артистов с главной страницы
    result = {}
    html_list_info_artist = soup.find(
        'li', class_='t229__list_item').find_all('li', class_="t-menusub__list-item t-name t-name_xs")
    for html_artist in html_list_info_artist:
        name_artist = html_artist.text.strip()
        url_card_artist = html_artist.find(
            'a', class_="t-menusub__link-item t-name t-name_xs").get('href').strip()
        result[name_artist] = url_card_artist
    return result



def pars_url_product(dict_artist_url):# сбор наименований и ссылок на товары с карточки артиста
    dict_position = {}
    for artist in dict_artist_url:
        url = f'https://glamgo.store{dict_artist_url[artist]}'
        soup = get_soup_from_selenium(url)
        html_position = soup.find_all(
            'div', class_="js-product t-store__card t-col t-col_4 t-align_center t-item")
        dict_position[artist] = {}
        for position in html_position:

            name = position.find(
                'div', class_="js-store-prod-name js-product-name t-store__card__title t-typography__title t-name t-name_md").text.strip()
            href = position.find('a').get('href')
            dict_position[artist][name] = href
        if html_position == []:
            dict_position[artist] = {None: None}

    return dict_position


def pars_from_card_product(url):  # сбор информации со страницы товара
    soup = get_soup(url)
    name = soup.find_all('div', class_='t-store__prod-popup__title-wrapper')
    price = soup.find_all(
        'div', class_='js-product-price js-store-prod-price-val t-store__prod-popup__price-value')
    chars = soup.find_all('p', class_='js-store-prod-charcs')

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
        'types': types,
        'color': color,
        'structure': structure,
        'application_chest': application_chest,
        'application_back': application_back,
    }
    return chars_name

def pars_url_img(dict_position):#парс ссылки на главную картинку карточек товаров
    dict_img = {}
    for artist in dict_position:
        dict_img[artist] = {}
        for product in dict_position[artist]:
            if product != None:
                # print(dict_position[artist])
                print(artist, product)
                soup = get_soup_from_selenium(dict_position[artist][product])
                try:
                    href = soup.find(
                    'div', class_='t-slds__bgimg t-bgimg js-product-img loaded').get('data-original')
                except AttributeError:
                    href = soup.find(
                        'meta', itemprop='image').get('content')
                dict_img[artist][product] = href
            else:
                dict_img[artist] = {None: None}
                
    return dict_img
                
            
            
        
    

