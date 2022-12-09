from distutils.util import change_root
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default.take_contact import keyboard_uzb
from states.taking_problem import ProblemDataUzbek
from keyboards.inline.uzbek_questions import return_questions_state_uzb
from keyboards.inline.callback_data import uzbek_questions_callback
from aiogram.types import ContentType
from keyboards.default.uzbek_keyboard import uzbek_menu
from data.config import GROUP_CHAT_ID
from states.time_tabel_giver import TTable
from keyboards.inline.stations import *
from keyboards.inline.auto_answer import answers


from loader import dp, bot

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='another'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Murojaat mavzusini tasvirlab bering, operator tez orada siz bilan bog'lanadi.
E'tiboringiz uchun tashakkur """, reply_markup=return_questions_state_uzb)
    await call.message.delete()
    await ProblemDataUzbek.problem_uzb.set()

@dp.message_handler(text = 'Qatnovlar Jadvali', state = ProblemDataUzbek.problem_uzb)
async def send_questions(message : types.Message, state = FSMContext):
    await state.reset_state()
    await bot.send_message(chat_id=message.chat.id, text="Shaharni tanlang", reply_markup=stations_uzb)
    await message.delete()
    await TTable.city_uzb.set()

@dp.message_handler(state=ProblemDataUzbek.problem_uzb)
async def take_problem(message:types.Message, state: FSMContext):
    problem = message.text
    await state.update_data(
        {"problem" : problem}
    )
    await message.answer("O'z kontaktingiz bilan bo'lishing iltimos", reply_markup=keyboard_uzb)
    await ProblemDataUzbek.number_uzb.set()

@dp.message_handler(state=ProblemDataUzbek.number_uzb, content_types=ContentType.CONTACT)
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
    await bot.send_message(chat_id=GROUP_CHAT_ID, text=f"Muammo: {problem}\nraqam : {num}\nuser : @{user}", reply_markup=answers)

    await state.reset_state()
    await message.answer("Murojaat mavzusini tasvirlab bering, operator tez orada siz bilan bog'lanadi.\nE'tiboringiz uchun tashakkur", reply_markup = uzbek_menu)

@dp.callback_query_handler(text="mycontact_uzb")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text='Kontaktingizni ulashing', reply_markup=keyboard_uzb)
    await call.message.delete()