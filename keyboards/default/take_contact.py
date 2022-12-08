from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_rus  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поделиться контактом', request_contact=True),
        ],
    ], 
resize_keyboard=True
)

keyboard_uzb  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kontaktni ulashish', request_contact=True),
        ],
    ], 
resize_keyboard=True

)