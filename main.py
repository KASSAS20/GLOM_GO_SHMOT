from bs4 import BeautifulSoup as bs
import requests
import pars_modul
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://glamgo.store/'
response = requests.get(url, headers=headers)

soup = bs(response.text, 'lxml')


dict_artist_url = pars_modul.pars_url_arists(soup)
pars_modul.pars_url_product(dict_artist_url)