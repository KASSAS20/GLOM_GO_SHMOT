from bs4 import BeautifulSoup as bs


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
    for i in dict_artist_url:
        print(i)