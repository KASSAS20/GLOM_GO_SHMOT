import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import pars_modul
import config

dict_artist = pars_modul.pars_url_arists()
dict_position = pars_modul.pars_url_product(dict_artist)

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
async def artist_check(message: types.Message):
    kb = []
    try:
        if message.text in dict_artist: # проверяем есть ли введёный артист в словаре
            for  position in dict_position[message.text]: # перебираем все товары
                kb.append([types.KeyboardButton(text=position)])#создаём кнопку с именем товара
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer(f'Выбери шмот', reply_markup=keyboard)
    except:# если у исполнителя на данный момент нет мерча
        await message.answer(f'У данного исполнителя нет мерча на данный момент')
        

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
