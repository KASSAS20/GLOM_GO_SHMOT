from bs4 import BeautifulSoup as bs
import requests
import pars_modul

# soup = pars_modul.get_soup('https://glamgo.store/')
# dict_artist_url = pars_modul.pars_url_arists(soup)
# dict_position = pars_modul.pars_url_product(dict_artist_url)

dict_position = {'GONE.Fludd': {'ФУТБОЛКА «DIGITAL FANTAZY»': 'https://glamgo.store/gonefludd/tproduct/237654106-747909980751-futbolka-digital-fantazy', 'ХУДИ «DIGITAL FANTAZY»': 'https://glamgo.store/gonefludd/tproduct/237654106-526584080341-hudi-digital-fantazy', 'СУМКА-ШОППЕР «DIGITAL FANTAZY»': 'https://glamgo.store/gonefludd/tproduct/237654106-956557525891-sumka-shopper-digital-fantazy', 'ФУТБОЛКА «DIGITAL EMOTIONS»': 'https://glamgo.store/gonefludd/tproduct/237654106-867236252641-futbolka-digital-emotions', 'ФУТБОЛКА "BAD BITCH", БЕЛАЯ': 'https://glamgo.store/gonefludd/tproduct/237654106-945415542771-futbolka-bad-bitch-belaya', 'ХУДИ «ВУДУ», ЧЕРНАЯ': 'https://glamgo.store/gonefludd/tproduct/237654106-670592902111-hudi-vudu-chernaya', 'ФУТБОЛКА «ILLFIGHTYOU»': 'https://glamgo.store/gonefludd/tproduct/237654106-668119489601-futbolka-illfightyou', "ФУТБОЛКА «PENI'S»": 'https://glamgo.store/gonefludd/tproduct/237654106-894113459421-futbolka-penis'}, 'CAKEBOY': {'ФУТБОЛКА «SMILES»': 'https://glamgo.store/cakeboy/tproduct/237841683-283757633041-futbolka-smiles', 'ФУТБОЛКА «HAIRSTYLE»': 'https://glamgo.store/cakeboy/tproduct/237841683-354370475801-futbolka-hairstyle', 'ХУДИ «ОКОЛЬНЫЙ ПУТЬ НА ЗАПАД»': 'https://glamgo.store/cakeboy/tproduct/237841683-694602504431-hudi-okolnii-put-na-zapad'}, 'IROH': {'ФУТБОЛКА «XANNY»': 'https://glamgo.store/iroh/tproduct/237840861-165835212961-futbolka-xanny'}, 'Flipper Floyd': {None: None}, 'GLAM GO!': {'КОМИКС «GLAM GO GANG!» МЯГКИЙ ПЕРЕПЛЕТ': 'https://glamgo.store/glamgo/tproduct/237841904-495453808761-komiks-glam-go-gang-myagkii-pereplet', '«GLAM GO BLING»': 'https://glamgo.store/glamgo/tproduct/237841904-319959646131-glam-go-bling', 'ФУТБОЛКА "GLAM GO"': 'https://glamgo.store/glamgo/tproduct/237841904-590850914901-futbolka-glam-go'}}

dict_img = pars_modul.pars_url_img(dict_position)
print(dict_img)