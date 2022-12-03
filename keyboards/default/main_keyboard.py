from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вопросы'),
        ],
    ], 
resize_keyboard=True

)