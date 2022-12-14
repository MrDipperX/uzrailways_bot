from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import *

questions_dict = {"Как купить билет" : "buy_ticket",
        'Получение pdf билета':'pdf',
        'Возврат билета': 'cancel',
        'Счет фактура билета':'schet',
        'Скидки на билеты':'discount',
        'Поменять билет':'change',
        'Регистрация на платформе':'registration',
        'Посадка без паспорта' : 'no_passport',
        'Новые вагоны и направления' : 'new_train',
        'Другая тема' : 'another'}

russian_questions = InlineKeyboardMarkup(row_width=1)
for key, value in questions_dict.items():
    russian_questions.insert(InlineKeyboardButton(text=key, callback_data = russian_questions_callback.new(item_name=value)))

return_questions_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='return_rus')
        ]
    ]
)

return_questions_state_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='return_state_rus')
        ]
    ]
)