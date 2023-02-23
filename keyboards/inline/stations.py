from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.lang import phrases

all_stations = {
    '2900002': 'Toshkent',
    '2900700': 'Samarqand',
    '2900800': 'Buxoro',
    '2900172': 'Xiva',
    '2900790': 'Urganch',
    '2900970': 'Nukus',
    '2900680': 'Andijon',
    '2900750': 'Qarshi',
    '2900720': 'Jizzax',
    '2900255': 'Termiz',
    '2900850': 'Guliston',
    '2900880': "Qo'qon",
    '2900920': "Marg'ilon",
    '2900693': "Pop",
    '2900940': "Namangan"
}


async def give_stations(source):
    number = 0
    inline_stations = InlineKeyboardMarkup(row_width=6)
    inline_stations.row()
    for value,key in all_stations.items():
        if value == source:
            continue
        if number % 3 == 0:
            inline_stations.row()
        inline_stations.insert(InlineKeyboardButton(
        key, callback_data=value
        ))
        number += 1
    inline_stations.row()
    if source is None:
        inline_stations.insert(InlineKeyboardButton(
            text='Ortga', callback_data='orqaga_st'
            ))
    else:
        inline_stations.insert(InlineKeyboardButton(
            text='Ortga', callback_data='orqaga_source'
            ))
    return inline_stations


