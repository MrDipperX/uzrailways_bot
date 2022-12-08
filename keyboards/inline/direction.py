from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

direction_rus = InlineKeyboardMarkup(
inline_keyboard=[
    [ 
        InlineKeyboardButton(text='Отправление', callback_data='go'),
        InlineKeyboardButton(text='Прибытие', callback_data='come'),
        
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='return_stations'),
    ]
])

direction_uzb = InlineKeyboardMarkup(
inline_keyboard=[
    [ 
        InlineKeyboardButton(text="Jo'nash", callback_data='go_uzb'),
        InlineKeyboardButton(text="Kelish", callback_data='come_uzb'),
        
    ],
    [
        InlineKeyboardButton(text='Ortga', callback_data='return_stations_uzb'),
    ]
])