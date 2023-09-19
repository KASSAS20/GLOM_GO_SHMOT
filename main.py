from bs4 import BeautifulSoup as bs
import requests
import pars_modul

# soup = pars_modul.get_soup('https://glamgo.store/')
# dict_artist_url = pars_modul.pars_url_arists(soup)
# dict_position = pars_modul.pars_url_product(dict_artist_url)

dict_position = {'CAKEBOY': {'ФУТБОЛКА «SMILES»': 'https://glamgo.store/cakeboy/tproduct/237841683-283757633041-futbolka-smiles', 'ФУТБОЛКА «HAIRSTYLE»': 'https://glamgo.store/cakeboy/tproduct/237841683-354370475801-futbolka-hairstyle', 'ХУДИ «ОКОЛЬНЫЙ ПУТЬ НА ЗАПАД»': 'https://glamgo.store/cakeboy/tproduct/237841683-694602504431-hudi-okolnii-put-na-zapad'}, 'IROH': {'ФУТБОЛКА «XANNY»': 'https://glamgo.store/iroh/tproduct/237840861-165835212961-futbolka-xanny'}, 'Flipper Floyd': {None: None}}

dict_img = pars_modul.pars_url_img(dict_position)
print(dict_img)