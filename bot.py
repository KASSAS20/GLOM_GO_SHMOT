import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import pars_modul
import config
import sqlite3

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

cursor.execute('''SELECT * FROM parsing_data''')
data = cursor.fetchall()

artist_dict = {}
data_dict = {}

for i in data:
    if i[0] not in artist_dict:
        artist_dict[i[0]] = i[1]

    data_dict[i[2]] = [i[0],i[3], i[5], i[6], i[7], i[8], i[9], i[10], i[4]]



# dict_artist = pars_modul.pars_url_arists() # словарь {artist:url_artist}
# dict_position = pars_modul.pars_url_product(dict_artist) # словарь {artist:{product:url_product}}
# list_product = []  # список со всеми продуктами сайта
# for artist in dict_artist:
#     for product in dict_position[artist]:
#         list_product.append(product)


logging.basicConfig(level=logging.INFO)# Включаем логирование, чтобы не пропустить важные сообщения

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = []
    for artist in artist_dict:
        kb.append([types.KeyboardButton(text=artist)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выбирите артиста", reply_markup=keyboard)


@dp.message()
async def button(message: types.Message):
    kb = []
    if message.text in artist_dict: # проверяем есть ли введёный артист в словаре
        for position in data_dict: # перебираем все товары
            print(position)
            if position != None and data_dict[position][0] == message.text:
                kb.append([types.KeyboardButton(text=position)])#создаём кнопку с именем товара
        kb.append([types.KeyboardButton(text='Домой')])
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(f'Выбери шмот', reply_markup=keyboard)
    
    elif message.text == 'Домой':
        await cmd_start(message)


    elif message.text in data_dict:
        for product in data_dict:
            # print(data_dict[message.text])
            if product == message.text:
                price = data_dict[message.text][2]
                type_product = data_dict[message.text][3]
                color = data_dict[message.text][4]
                structur = data_dict[message.text][5]
                application_chest = data_dict[message.text][6]
                application_back = data_dict[message.text][7]
                img = data_dict[message.text][8]
                # message_text = <a href = 'https://example.com' style = 'display:none;' > кликните здесь < /a >

                mes = f'Товар: <a href="{img}" style="display:none;">{product}</a>\nЦена: {price}руб.\n{type_product}\n{color}\n{structur}\n{application_chest}\n{application_back}'
                while 'None' in mes:
                    mes = mes.replace('None', '')
                await message.answer(mes, parse_mode='HTML')
    else:
        await message.answer('Ты говоришь на непонятном мне языке')
                    
    
        

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
