from atexit import register
from cgitb import text
from re import U
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery
from keyboards.inline.questions import questions, return_questions
from keyboards.inline.callback_data import questions_callback
from states.taking_problem import ProblemData
from aiogram.dispatcher import FSMContext

from loader import dp, bot

@dp.callback_query_handler(questions_callback.filter(item_name='pdf'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Что бы скачать pdf билета на сайте:
1. Нажмите на "Логин"
2. Выберите "Мои новые заказы"
3. Выберите "Распечатать заказ"
Что бы скачать билет в приложении: 
1. Нажмите на "Заказы"
2. Выберите "Получить бланк заказа". 
Билет будет скачан на телефон в папку "мои файлы" """, reply_markup=return_questions)
    await call.message.delete()

@dp.callback_query_handler(questions_callback.filter(item_name='cancel'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для возврата билета войдите в личный кабинет с логином с которого был куплен билет:
1. Нажмите на "Логин"
2. Выберите "Мои новые заказы"
3. Выберите "Подробнее"
4. Выберите "Вернуть билет". 
Возврат денег осуществится в течении 3-5 рабочих дней (15 рабочих дней, если карта оплаты была международной)  на ту же карту с которого был куплен билет.  
Также возврат билета возможен железно-дорожных кассах Узбекистана.""", reply_markup=return_questions)
    await call.message.delete()


@dp.callback_query_handler(questions_callback.filter(item_name='schet'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для получении счет фактуры после покупки билета:
1. Нажмите на кнопку "получить счет фактуру"
2. Введите ИНН компании привязанный к карте Счет фактура придет автоматический на следующий рабочий день. 
Если вы не получили счет фактуру просим связаться с нами в боте:
1. Выбрав тему обращения "Другая тема" """, reply_markup=return_questions)
    await call.message.delete()
    await call.answer(cache_time=10)

@dp.callback_query_handler(questions_callback.filter(item_name='change'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Что бы поменять билет, вы должны возвратить билет и купить билет на другую дату. Для возврата билета войдите в личный кабинет с логином с которого был куплен билет:
1. Нажмите на "Логин"
2. Выберите "Мои новые заказы"
3. Выберите "Подробнее"
4. Выберите "Вернуть билет". 
Возврат денег осуществится в течении 3-5 рабочих дней (15 рабочих дней, если карта оплаты была международной)  на ту же карту с которого был куплен билет.  
Также возврат билета возможен железно-дорожных кассах Узбекистана.""", reply_markup=return_questions)
    await call.message.delete()

@dp.callback_query_handler(questions_callback.filter(item_name='discount'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для получения информации о скидках и акциях, позвоните в справочную по номеру 1005""", reply_markup=return_questions)
    await call.message.delete()
    await call.answer(cache_time=10)

@dp.callback_query_handler(questions_callback.filter(item_name='registration'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Для регистрации в платформе:
1. Перейдите на страницу https://chipta.railway.uz/ru/auth/register
2. Укажите свой email или номер телефона.
3. Введите пароль
4. Повторите введенный пароль
5. Нажмите "Зарегистрироваться" """, reply_markup=return_questions)
    await call.message.delete()

@dp.callback_query_handler(text='return')
async def return_to_questions(call: CallbackQuery):
    await call.message.answer("Выберите тему обращения", reply_markup=questions)
    await call.message.delete()

@dp.callback_query_handler(text='return_state', state=ProblemData.problem)
async def return_to_questions(call: CallbackQuery,state : FSMContext):
    await state.reset_state()
    await call.message.answer("Выберите тему обращения", reply_markup=questions)
    await call.message.delete()



