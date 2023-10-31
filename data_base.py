import sqlite3
import pars_modul as pars
import os

file_path = "data.db"
try:
    os.remove(file_path)
    print(f"Файл {file_path} успешно удален.")
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except Exception as e:
    print(f"Произошла ошибка при удалении файла: {e}")


connect_data = sqlite3.connect("data.db")
data = connect_data.cursor()

data.execute('''CREATE TABLE IF NOT EXISTS parsing_data(
                artist TEXT,
                url_artist TEXT,
                product TEXT,
                product_url TEXT,
                product_img TEXT,
                price TEXT,
                types TEXT,
                color TEXT,
                structure TEXT,
                application_chest TEXT,
                application_back TEXT)''')

url_artist_dict = pars.pars_url_arists()
url_product_dict = pars.pars_url_product(url_artist_dict)
img_dict = pars.pars_url_img(url_product_dict)

for artist in url_artist_dict:
    url_artist = url_artist_dict[artist]  # url_artist
    for product in url_product_dict[artist]:  # product
        url_product = url_product_dict[artist][product]  # url product
        if url_product != None:
            info_product = pars.pars_from_card_product(
                url_product)  # info product
            price = str(info_product['price'])
            types = str(info_product['types'])
            color = str(info_product['color'])
            structure = str(info_product['structure'])
            application_chest = str(info_product['application_chest'])
            application_back = str(info_product['application_back'])
            url_img = img_dict[artist][product]  # img
        else:
            price = None
            types = None
            color = None
            structure = None
            application_chest = None
            application_back = None
            url_img = None

        data.execute('''INSERT INTO parsing_data VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (artist, url_artist,
                     product, url_product, url_img, price, types, color, structure, application_chest, application_back))
        connect_data.commit()

connect_data.close()
