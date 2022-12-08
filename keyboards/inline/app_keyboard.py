from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import *

app_divider = {"Приложение" : "programm",
                "Веб-сайт" : "site"}

return_questions_rus = InlineKeyboardButton(text='Назад', callback_data='return_rus')

pdf_divisor = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    pdf_divisor.insert(InlineKeyboardButton(text=key, callback_data = pdf_callback.new(item_name=value)))
pdf_divisor.insert(return_questions_rus)

ticket_return = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    ticket_return.insert(InlineKeyboardButton(text=key, callback_data = ticket_return_callback.new(item_name=value)))
ticket_return.insert(return_questions_rus)

faktura = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    faktura.insert(InlineKeyboardButton(text=key, callback_data = faktura_callback.new(item_name=value)))
faktura.insert(return_questions_rus)

discount = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    discount.insert(InlineKeyboardButton(text=key, callback_data = discount_callback.new(item_name=value)))
discount.insert(return_questions_rus)

change_ticket = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    change_ticket.insert(InlineKeyboardButton(text=key, callback_data = change_ticket_callback.new(item_name=value)))
change_ticket.insert(return_questions_rus)

registration = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider.items():
    registration.insert(InlineKeyboardButton(text=key, callback_data = registration_callback.new(item_name=value)))
registration.insert(return_questions_rus)

app_divider_uzb = {"Mobil ilova" : "programm_uzb",
                "Web-sahifa" : "site_uzb"}

return_questions_uzb = InlineKeyboardButton(text='Ortga', callback_data='return_uzb')

pdf_divisor_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    pdf_divisor_uzb.insert(InlineKeyboardButton(text=key, callback_data = pdf_callback_uzb.new(item_name=value)))
pdf_divisor_uzb.insert(return_questions_uzb)

ticket_return_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    ticket_return_uzb.insert(InlineKeyboardButton(text=key, callback_data = ticket_return_callback_uzb.new(item_name=value)))
ticket_return_uzb.insert(return_questions_uzb)

faktura_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    faktura_uzb.insert(InlineKeyboardButton(text=key, callback_data = faktura_callback_uzb.new(item_name=value)))
faktura_uzb.insert(return_questions_uzb)

discount_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    discount_uzb.insert(InlineKeyboardButton(text=key, callback_data = discount_callback_uzb.new(item_name=value)))
discount_uzb.insert(return_questions_uzb)

change_ticket_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    change_ticket_uzb.insert(InlineKeyboardButton(text=key, callback_data = change_ticket_callback_uzb.new(item_name=value)))
change_ticket_uzb.insert(return_questions_uzb)

registration_uzb = InlineKeyboardMarkup(row_width=1)
for key, value in app_divider_uzb.items():
    registration_uzb.insert(InlineKeyboardButton(text=key, callback_data = registration_callback_uzb.new(item_name=value)))
registration_uzb.insert(return_questions_uzb)
