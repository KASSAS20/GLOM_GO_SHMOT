from bs4 import BeautifulSoup as bs
import requests
import pars_modul

soup = pars_modul.get_soup('https://glamgo.store/')
dict_artist_url = pars_modul.pars_url_arists(soup)
pars_modul.pars_url_product(dict_artist_url)