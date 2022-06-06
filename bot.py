from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import asyncio
import os
import json
import time

from aiogram.utils.markdown import hbold, hlink
from main import collect_data
bot = Bot(token='5508832970:AAESzeWx-o43BFQesNtGmp6gH7b-GYwIbDo', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Ножи👅', 'Перчатки 🧤', 'AWP 🤡']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Привет, бот предназначен для парсинга айтемов с маркетплейса cs.money \n Бот выдает запрос по скинам, которые имеют скидку более 10 процентов')
    await message.answer('Выберите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='Ножи👅'))
async def get_discount_knifes(message: types.Message):
    await message.answer('Ожидайте пожалуйста, вытряхиваем инфу с сайта')

    collect_data(types=2)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n' \
               f'{hbold('Скидочка: ')}{item.get('overprice')}% 🦾\n' \
               f'{hbold('Цена: ')}${item.get('item_price')}🍔"

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)


@dp.message_handler(Text(equals='AWP 🤡'))
async def get_discount_knifes(message: types.Message):
    await message.answer('Ожидайте пожалуйста, вытряхиваем инфу с сайта')

    collect_data(types=4)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n' \
               f'{hbold('Скидочка: ')}{item.get('overprice')}% 🦾\n' \
               f'{hbold('Цена: ')}${item.get('item_price')}🍔"

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)

@dp.message_handler(Text(equals='Перчатки 🧤'))
async def get_discount_knifes(message: types.Message):
    await message.answer('Ожидайте пожалуйста, вытряхиваем инфу с сайта')

    collect_data(types=13)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'), item.get('3d'))}\n' \
               f'{hbold('Скидочка: ')}{item.get('overprice')}% 🦾\n' \
               f'{hbold('Цена: ')}${item.get('item_price')}🍔"

        if index%20 == 0:
            time.sleep(3)
        await message.answer(card)


def main():
    executor.start_polling(dp)

if __name__=='__main__':
    main()