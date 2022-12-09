from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

answers = InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text='✅', callback_data='done'),
    ]
])