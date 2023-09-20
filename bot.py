import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import pars_modul
import config

dict_artist = pars_modul.pars_url_arists() # словарь {artist:url_artist}
dict_position = pars_modul.pars_url_product(dict_artist) # словарь {artist:{product:url_product}}
list_product = []  # список со всеми продуктами сайта
for artist in dict_artist:
    for product in dict_position[artist]:
        list_product.append(product)


print(list_product)
logging.basicConfig(level=logging.INFO)# Включаем логирование, чтобы не пропустить важные сообщения

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = []
    for artist in dict_artist:
        kb.append([types.KeyboardButton(text=artist)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Выбирите артиста", reply_markup=keyboard)


@dp.message()
async def button(message: types.Message):
    kb = []
    try:
        if message.text in dict_artist: # проверяем есть ли введёный артист в словаре
            for  position in dict_position[message.text]: # перебираем все товары
                kb.append([types.KeyboardButton(text=position)])#создаём кнопку с именем товара
            kb.append([types.KeyboardButton(text='Домой')])
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer(f'Выбери шмот', reply_markup=keyboard)
    except:# если у исполнителя на данный момент нет мерча
        await message.answer(f'У данного исполнителя нет мерча на данный момент')
    
    if message.text == 'Домой':
        await cmd_start(message)

    elif message.text in list_product:
        for artist in dict_position:
            for product in dict_position[artist]:
                if product == message.text:
                    dict_card = pars_modul.pars_from_card_product(dict_position[artist][product])
                    print(dict_card)
                    name = dict_card['name']
                    price = dict_card['price']
                    type = dict_card['types']
                    color = dict_card['color']
                    structur = dict_card['structure']
                    application_chest = dict_card['application_chest']
                    application_back = dict_card['application_back']
                    if not application_chest or not application_back:
                        mes = f'Товар: {name}\nЦена: {price}руб.\n{type}\n{color}\n{structur}'
                    else:
                        mes = f'Товар: {name}\nЦена: {price}руб.\n{type}\n{color}\n{structur}\n{application_chest}\n{application_back}'
                    await message.answer(mes)
    elif message.text.lower() == 'иди нахуй':
        await message.answer('Не ругайся, бро')
    elif message.text not in dict_artist:
        await message.answer('Ты говоришь на непонятном мне языке')
                    
    
        

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
