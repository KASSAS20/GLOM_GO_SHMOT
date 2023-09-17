from bs4 import BeautifulSoup as bs


def pars_url_arists(soup):
    urls = soup.find_all('div')
    for i in urls:
        print(urls)