from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import questions_callback

questions_dict = {'Получение pdf билета':'pdf',
        'Возврат билета': 'cancel',
        'Счет фактура билета':'schet',
        'Поменять билет':'change',
        'Скидки на билеты':'discount',
        'Поменять билет':'change',
        'Регистрация в платформе':'registration',
        'Другая тема' : 'another'}

questions = InlineKeyboardMarkup(row_width=1)
for key, value in questions_dict.items():
    questions.insert(InlineKeyboardButton(text=key, callback_data = questions_callback.new(item_name=value)))

return_questions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='return')
        ]
    ]
)

return_questions_state = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='return_state')
        ]
    ]
)