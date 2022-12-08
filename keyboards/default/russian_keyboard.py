from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

russian_menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вопросы'),
        ],
        [
            KeyboardButton(text="Расписание")
        ]
    ], 
resize_keyboard=True

)