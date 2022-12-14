from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery
from keyboards.inline.russian_questions import russian_questions, return_questions_rus
from keyboards.inline.uzbek_questions import uzbek_questions, return_questions_state_uzb
from keyboards.inline.callback_data import *
from states.taking_problem import ProblemDataUzbek
from aiogram.dispatcher import FSMContext
from keyboards.inline.app_keyboard import *

from loader import dp, bot

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='pdf'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=pdf_divisor_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='buy_ticket'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=buying_ticket_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='cancel'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=ticket_return_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='schet'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=faktura_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='new_vagon'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Har kuni qo'shimcha vagonlar qo`shiladi. Batafsil ma'lumotni  veb-saytga kirib  yoki  ma`lumotxonaning  1005 qisqa raqamiga qo`ng`iroq qilib bilishingiz  mumkin.", reply_markup=return_questions_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='passport_no'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Poyezdga chiqish uchun yo`lovchi pdf ko`rinishidagi elektron chiptasini hamda chiptada ko`rsatilgan shaxsni tasdiqlovchi hujjat (pasport, IDkarta yoki yangi haydovchilik guvohnomasi) taqdim qilishi shart.""", reply_markup=return_questions_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='change'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""To'liq ma'lumotni olish uchun 1005 raqamiga qo'ng'iroq qiling""", reply_markup=return_questions_uzb)
    # await call.message.answer("O'z qurilmangizni tanlang", reply_markup=change_ticket_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='discount'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""To'liq ma'lumotni olish uchun 1005 raqamiga qo'ng'iroq qiling""", reply_markup=return_questions_uzb)
    # await call.message.answer("O'z qurilmangizni tanlang", reply_markup=discount_uzb)
    await call.message.delete()

@dp.callback_query_handler(uzbek_questions_callback.filter(item_name='registration'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=registration_uzb)
    await call.message.delete()

@dp.callback_query_handler(text='return_uzb')
async def return_to_questions(call: CallbackQuery):
    await call.message.answer("O'z qurilmangizni tanlang", reply_markup=uzbek_questions)
    await call.message.delete()

@dp.callback_query_handler(text='return_state_uzb', state=ProblemDataUzbek.problem_uzb)
async def return_to_questions(call: CallbackQuery,state : FSMContext):
    await state.reset_state()
    await call.message.answer("Murojaatingiz mavzusini tanlang", reply_markup=uzbek_questions)
    await call.message.delete()