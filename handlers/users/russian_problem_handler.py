from distutils.util import change_root
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default.take_contact import keyboard_rus
from aiogram.types import ReplyKeyboardRemove
from states.taking_problem import ProblemData
from keyboards.inline.callback_data import russian_questions_callback, uzbek_questions_callback
from keyboards.inline.get_contact import getting_contact_russian
from keyboards.inline.russian_questions import return_questions_rus, return_questions_state_rus
from aiogram.types import ContentType
from keyboards.default.russian_keyboard import russian_menu
from data.config import GROUP_CHAT_ID
from keyboards.inline.auto_answer import answers
from states.time_tabel_giver import TTable
from keyboards.inline.stations import *


from loader import dp, bot

@dp.callback_query_handler(russian_questions_callback.filter(item_name='another'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Опишите вашу тему обращения, в скором времени с вами свяжется оператор.
Благодарим вас за внимание """, reply_markup=return_questions_state_rus)
    await call.message.delete()
    await ProblemData.problem.set()

@dp.message_handler(text = 'Расписание', state=ProblemData.problem)
async def send_questions(message : types.Message, state = FSMContext):
    await state.reset_state()
    await message.answer("Выберите город", reply_markup=stations_rus)
    await message.delete()
    await TTable.city.set()

@dp.message_handler(state=ProblemData.problem)
async def take_problem(message:types.Message, state: FSMContext):
    problem = message.text
    await state.update_data(
        {"problem" : problem}
    )
    await message.answer("Поделитесь контактом пожалуйста", reply_markup=keyboard_rus)
    await ProblemData.number.set()

@dp.message_handler(state=ProblemData.number, content_types=ContentType.CONTACT)
async def take_phone(message: types.Contact, state : FSMContext):
    phone = message.contact.phone_number
    username = message.from_user.username
    await state.update_data(
        {'phone' : phone, 'user' : username}
    )

    data = await state.get_data()
    problem = data.get('problem')
    num = data.get('phone')
    user = data.get('user')
    await message.answer("Спасибо, в скором времени с вами свяжется оператор.\nБлагодарим вас за внимание", reply_markup = russian_menu)
    await bot.send_message(chat_id=GROUP_CHAT_ID, text=f"Проблема: {problem}\nномер : {num}\nюзер : @{user}", reply_markup=answers)
    await state.reset_state()

@dp.callback_query_handler(text="mycontact_rus")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text='Поделитесь контаком', reply_markup=keyboard_rus)
    await call.message.delete()

@dp.callback_query_handler(text="done")
async def show_contact_keys(call: CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id, 
        reply_markup=None
    )