from distutils.util import change_root
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_keyboard import menu
from keyboards.inline.questions import questions

from loader import dp, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
        await bot.send_message(chat_id = message.chat.id, text = "Здравствуйте. Это автоматический бот поддержки Uzrailways", reply_markup=menu)
        await message.delete()

@dp.message_handler(text = 'Вопросы')
async def send_questions(message : types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Выберите тему обращения", reply_markup=questions)
    await message.delete()