e = {'CAKEBOY': {'ФУТБОЛКА «SMILES»': 'https://static.tildacdn.com/tild3932-6164-4736-a538-363338666433/4.jpg', 'ФУТБОЛКА «HAIRSTYLE»': 'https://static.tildacdn.com/tild3236-6633-4737-b438-396265663062/photo.jpg', 'ХУДИ «ОКОЛЬНЫЙ ПУТЬ НА ЗАПАД»':
                 'https://static.tildacdn.com/tild3938-3366-4136-a436-343436313163/OP4i35tbaJo.jpg'}, 'IROH': {'ФУТБОЛКА «XANNY»': 'https://static.tildacdn.com/tild3235-3539-4632-a539-643238623233/photo_2020-10-28_00-.jpg'}, 'Flipper Floyd': {None: None}}

url = 'https://glamgo.store/iroh/tproduct/237840861-165835212961-futbolka-xanny'

import pars_modul
from bs4 import BeautifulSoup as bs
html = pars_modul.get_soup_from_selenium(url)

with open('product.html', 'w') as file:
    file.write(str(html))
    file.close()