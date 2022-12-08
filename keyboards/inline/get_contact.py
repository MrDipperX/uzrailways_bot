from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

getting_contact_russian = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Поделиться контактом", callback_data='mycontact_rus'),
    ]]
)

getting_contact_uzbek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Kontaktni ulashish", callback_data='mycontact_uzb'),
    ]]
)