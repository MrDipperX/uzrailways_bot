from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

stations_rus = InlineKeyboardMarkup(
inline_keyboard=[
    [ 
        InlineKeyboardButton(text='Ташкент', callback_data='2900001'),
        InlineKeyboardButton(text='Самарканд', callback_data='2900700'),
        InlineKeyboardButton(text='Бухара', callback_data='2900800'),
    ],
    [
        InlineKeyboardButton(text='Хива', callback_data='2900172'),
        InlineKeyboardButton(text='Ургенч', callback_data='2900790'),
        InlineKeyboardButton(text='Нукус', callback_data='2900970'),
    ],
    [
        InlineKeyboardButton(text='Навои', callback_data='2900930'),
        InlineKeyboardButton(text='Карши', callback_data='2900750'),
        InlineKeyboardButton(text='Джизак', callback_data='2900720'),
    ],
    [
        InlineKeyboardButton(text='Термез', callback_data='2900255'),
        InlineKeyboardButton(text='Гулистан', callback_data='2900850'),
    ]
])

stations_uzb = InlineKeyboardMarkup(
inline_keyboard=[
    [ 
        InlineKeyboardButton(text='Toshkent', callback_data='2900001'),
        InlineKeyboardButton(text='Samarqand', callback_data='2900700'),
        InlineKeyboardButton(text='Buxoro', callback_data='2900800'),
    ],
    [
        InlineKeyboardButton(text='Xiva', callback_data='2900172'),
        InlineKeyboardButton(text='Urganch', callback_data='2900790'),
        InlineKeyboardButton(text='Nukus', callback_data='2900970'),
    ],
    [
        InlineKeyboardButton(text='Navoiy', callback_data='2900930'),
        InlineKeyboardButton(text='Qarshi', callback_data='2900750'),
        InlineKeyboardButton(text='Jizzax', callback_data='2900720'),
    ],
    [
        InlineKeyboardButton(text='Termiz', callback_data='2900255'),
        InlineKeyboardButton(text='Guliston', callback_data='2900850'),
    ]
])


