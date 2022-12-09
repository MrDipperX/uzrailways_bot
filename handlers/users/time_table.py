from distutils.util import change_root
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_keyboard import menu
from keyboards.default.russian_keyboard import russian_menu
from keyboards.default.uzbek_keyboard import uzbek_menu
from keyboards.inline.russian_questions import russian_questions
from keyboards.inline.uzbek_questions import uzbek_questions
from keyboards.inline.stations import *
from states.time_tabel_giver import TTable
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.direction import *
import requests
from data.config import RAILWAY_API

from loader import dp, bot

@dp.message_handler(text = 'Расписание')
async def send_questions(message : types.Message):
    await message.answer("Выберите город", reply_markup=stations_rus)
    await message.delete()
    await TTable.city.set()


@dp.callback_query_handler(state=TTable.city)
async def send_direction(call: CallbackQuery, state = FSMContext):
    city = int(call.data)
    await state.update_data(
        {"city" : city}
    )
    await bot.send_message(chat_id=call.from_user.id, text="Выберите направление пожалуйста", reply_markup=direction_rus)
    await call.message.delete()
    await TTable.direction.set()

@dp.callback_query_handler(state=TTable.city_uzb)
async def send_direction(call: CallbackQuery, state = FSMContext):
    city = int(call.data)
    await state.update_data(
        {"city" : city}
    )
    await bot.send_message(chat_id=call.from_user.id, text="Yo'nalishni tanlang iltimos", reply_markup=direction_uzb)
    await call.message.delete()
    await TTable.direction.set()

@dp.callback_query_handler(text = 'return_stations', state=TTable.direction)
async def send_questions(call: CallbackQuery, state = FSMContext):
    await state.reset_state()
    await call.message.answer("Выберите город", reply_markup=stations_rus)
    await call.message.delete()
    await TTable.city.set()

@dp.callback_query_handler(text = 'return_stations_uzb', state=TTable.direction)
async def send_questions(call: CallbackQuery, state = FSMContext):
    await state.reset_state()
    await call.message.answer("Shaharni tanlang", reply_markup=stations_uzb)
    await call.message.delete()
    await TTable.city_uzb.set()

@dp.message_handler(text = 'Qatnovlar Jadvali')
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Shaharni tanlang", reply_markup=stations_uzb)
    await message.delete()
    await TTable.city_uzb.set()

@dp.callback_query_handler(state=TTable.direction)
async def send_direction(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data.get('city')
    API = RAILWAY_API
    headers = {"Content-Type": "application/json", "Accept-Language" : "uz", }
    data = {"code":int(city)}
    r = requests.post(url = API,headers=headers, json = data)
    dict_values = {}
    if "go" in call.data:
        for train in r.json()['depTrains']['train']:
            dict_values[train['depTime']] = train['route']['station']
            dict_values[train['depTime']].append(train['number'])
            dict_values[train['depTime']].append(train['brand'])
        result = '\\n'.join(f'{key}   {value[2]}   {value[0]} : {value[1]}({value[3]})' for key, value in dict_values.items())
        result = result.replace('\\n', '\n').replace("None", "").replace("()", "")
        if len(result) == 0:
            if call.data == "go_uzb":
                await bot.send_message(chat_id=call.from_user.id, text="Yo'nalish bo'yicha poyezdlar yo'q")
            else:
                await bot.send_message(chat_id=call.from_user.id, text="По этому направлению поездов нет")
        else:
            await bot.send_message(chat_id=call.from_user.id, text=result)
        await call.message.delete()
        await state.reset_state()
    elif "come" in call.data:
        for train in r.json()['arvTrains']['train']:
            dict_values[train['arvTimeToStation']] = train['route']['station']
            dict_values[train['depTime']].append(train['number'])
            dict_values[train['depTime']].append(train['brand'])
        result = '\\n'.join(f'{key}   {value[2]}   {value[0]} : {value[1]}({value[3]})' for key, value in dict_values.items())
        result = result.replace('\\n', '\n').replace("None", "").replace("()", "")
        if len(result) == 0:
            if call.data == "come_uzb":
                await bot.send_message(chat_id=call.from_user.id, text="Yo'nalish bo'yicha poyezdlar yo'q")
            else:
                await bot.send_message(chat_id=call.from_user.id, text="По этому направлению поездов нет")
        else:
            await bot.send_message(chat_id=call.from_user.id, text=result)
        await call.message.delete()
        await state.reset_state()