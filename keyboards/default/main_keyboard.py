from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbeckcha"),
        ],
        [
            KeyboardButton(text="Русский"),
        ]
    ], 
resize_keyboard=True

)