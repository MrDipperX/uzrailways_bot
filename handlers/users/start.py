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

from loader import dp, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
        await bot.send_message(chat_id = message.chat.id, text = "Assalomu Alaykum. Tilni tanlang \nЗдравствуйте. Выберите язык", reply_markup=menu)
        await message.delete()

@dp.message_handler(text = 'Русский')
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Здравствуйте. Это автоматический бот поддержки Uzrailways", reply_markup=russian_menu)
    await message.delete()

@dp.message_handler(text = "O'zbeckcha")
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Assalomu Alaykum. Bu Uzrailways avtomatik qo'llab-quvvatlash boti", reply_markup=uzbek_menu)
    await message.delete()

@dp.message_handler(text = 'Вопросы', state=TTable.city)
async def send_questions(message : types.Message, state = FSMContext):
    await state.reset_state()
    await bot.send_message(chat_id=message.chat.id, text="Выберите тему обращения", reply_markup=russian_questions)
    await message.delete()

@dp.message_handler(text = 'Вопросы')
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Выберите тему обращения", reply_markup=russian_questions)
    await message.delete()

@dp.message_handler(text = 'Savollar')
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Murojaatingiz mavzusini tanlang", reply_markup=uzbek_questions)
    await message.delete()

@dp.message_handler(text = 'Savollar', state = TTable.city_uzb)
async def send_questions(message : types.Message, state = FSMContext):
    await state.reset_state()
    await bot.send_message(chat_id=message.chat.id, text="Murojaatingiz mavzusini tanlang", reply_markup=uzbek_questions)
    await message.delete()