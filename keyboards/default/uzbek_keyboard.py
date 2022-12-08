from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uzbek_menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Savollar'),
        ],
        [
            KeyboardButton(text="Qatnovlar Jadvali"),
        ]
    ], 
resize_keyboard=True

)