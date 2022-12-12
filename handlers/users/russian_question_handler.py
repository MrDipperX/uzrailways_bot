from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery
from keyboards.inline.russian_questions import russian_questions, return_questions_rus
from keyboards.inline.callback_data import *
from states.taking_problem import ProblemData
from aiogram.dispatcher import FSMContext
from keyboards.inline.app_keyboard import *

from loader import dp, bot

@dp.callback_query_handler(russian_questions_callback.filter(item_name='pdf'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Выберите ваше устройтсво", reply_markup=pdf_divisor)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='cancel'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Выберите ваше устройтсво", reply_markup=ticket_return)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='schet'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Выберите ваше устройтсво", reply_markup=faktura)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='new_train'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Каждый день цепляются дополнительные вагоны, для более подробной информации зайдите на сайт либо позвоните в справочную по короткому номеру 1005", reply_markup=return_questions_rus)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='no_passport'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("При посадке пассажир должен предъявить электронный билет в виде pdf файла и оригинал документа удостоверяющего личность (паспорт, ID-карта или водительские права нового образца)", reply_markup=return_questions_rus)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='change'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для получения информации, позвоните в справочную по номеру 1005""", reply_markup=return_questions_rus)
    # await call.message.answer("Выберите ваше устройтсво", reply_markup=change_ticket)
    await call.message.delete()


@dp.callback_query_handler(russian_questions_callback.filter(item_name='discount'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для получения информации о скидках и акциях, позвоните в справочную по номеру 1005""", reply_markup=return_questions_rus)
    # await call.message.answer("Выберите ваше устройтсво", reply_markup=discount)
    await call.message.delete()

@dp.callback_query_handler(russian_questions_callback.filter(item_name='registration'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Выберите ваше устройтсво", reply_markup=registration)
    await call.message.delete()

@dp.callback_query_handler(text='return_rus')
async def return_to_questions(call: CallbackQuery):
    await call.message.answer("Выберите тему обращения", reply_markup=russian_questions)
    await call.message.delete()

@dp.callback_query_handler(text='return_state_rus', state=ProblemData.problem)
async def return_to_questions(call: CallbackQuery,state : FSMContext):
    await state.reset_state()
    await call.message.answer("Выберите тему обращения", reply_markup=russian_questions)
    await call.message.delete()



