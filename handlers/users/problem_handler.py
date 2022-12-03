from distutils.util import change_root
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default.take_contact import keyboard
from aiogram.types import ReplyKeyboardRemove
from states.taking_problem import ProblemData
from keyboards.inline.callback_data import questions_callback
from keyboards.inline.get_contact import getting_contact
from keyboards.inline.questions import return_questions, return_questions_state
from aiogram.types import ContentType
from keyboards.default.main_keyboard import menu
from data.config import GROUP_CHAT_ID


from loader import dp, bot

@dp.callback_query_handler(questions_callback.filter(item_name='another'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("""Опишите вашу тему обращения, в скором времени с вами свяжется оператор.
Благодарим вас за внимание """, reply_markup=return_questions_state)
    await call.message.delete()
    await ProblemData.problem.set()

@dp.message_handler(state=ProblemData.problem)
async def take_problem(message:types.Message, state: FSMContext):
    problem = message.text
    await state.update_data(
        {"problem" : problem}
    )
    # await state.reset_state(with_data=False)
    await message.answer("Поделитесь контактом пожалуйста", reply_markup=keyboard)
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
    await bot.send_message(chat_id=GROUP_CHAT_ID, text=f"Проблема: {problem}\nномер : {num}\nюзер : @{user}")

    await state.reset_state()
    await message.answer("Спасибо, в скором времени с вами свяжется оператор.\nБлагодарим вас за внимание", reply_markup = menu)

@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text='Поделитесь контаком', reply_markup=keyboard)
    await call.message.delete()

@dp.message_handler(content_types='contact')
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(f"Спасибо {contact.full_name} \
 скоро с вами свяжется оператор", reply_markup=ReplyKeyboardRemove())