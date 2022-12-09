from distutils.util import change_root
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from itertools import count
from xml.dom.domreg import registered
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import ContentType
from keyboards.default.russian_keyboard import russian_menu
from data.config import *
from keyboards.inline.auto_answer import answers
from keyboards.inline.callback_data import *

from loader import dp, bot

@dp.message_handler(content_types=ContentType.PHOTO)
async def download(message: types.Message):
    # print(message.file_id)
    print(message.photo[0].file_id)
    await bot.send_message(chat_id=message.from_user.id, text=message.photo[0].file_id)

@dp.callback_query_handler(pdf_callback.filter(item_name='site'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Получение pdf билета")
    for image in PDF_QUESTION_RUS:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(pdf_callback.filter(item_name='programm'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("В процессе скоро все дополним ...")
    await call.message.delete()

@dp.callback_query_handler(ticket_return_callback.filter(item_name='site'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Возврат билета на веб-сайте")
    for image in RETURN_TICKET_RUS:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(ticket_return_callback.filter(item_name='programm'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Возврат билета в приложении")
    for image in RETURN_TICKET_RUS_APP:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(faktura_callback.filter(item_name='site'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Получение счет фактуры")
    for image in FAKTURA_RUS:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(faktura_callback.filter(item_name='programm'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("В процессе скоро все дополним ...")
    await call.message.delete()

# @dp.callback_query_handler(discount_callback.filter(item_name='site'))
# async def answer_question(call: CallbackQuery, callback_data:dict):
#     await call.message.reply_photo(photo="AgACAgIAAxkBAAIEQmOQh_e9biU5CkBxRRwS9Oavi1iqAAKqwTEbHAeISCwZTHOIByW8AQADAgADcwADKwQ", caption="2836123")
#     await call.message.delete()

# @dp.callback_query_handler(change_ticket_callback.filter(item_name='site'))
# async def answer_question(call: CallbackQuery, callback_data:dict):
#     await call.message.reply_photo(photo="AgACAgIAAxkBAAIEQmOQh_e9biU5CkBxRRwS9Oavi1iqAAKqwTEbHAeISCwZTHOIByW8AQADAgADcwADKwQ", caption="2836123")
#     await call.message.delete()

@dp.callback_query_handler(registration_callback.filter(item_name='site'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Регистрация на веб-сайте")
    for image in REGISTRATION_RUS:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(registration_callback.filter(item_name='programm'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("В процессе скоро все дополним ...")
    await call.message.delete()


#UZbek part
@dp.callback_query_handler(pdf_callback_uzb.filter(item_name='site_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Biletni pdf shaklini yuklab olish")
    for image in PDF_QUESTION_UZB:
      await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(pdf_callback_uzb.filter(item_name='programm_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Jarayonda tez orada qo'shiladi ...")
    await call.message.delete()

@dp.callback_query_handler(ticket_return_callback_uzb.filter(item_name='site_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Biletni web-sahifada qaytarib berish")
    for image in RETURN_TICKET_UZB:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(ticket_return_callback_uzb.filter(item_name='programm_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Biletni mobil ilovada qaytarib berish")
    for image in RETURN_TICKET_UZB_APP:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(faktura_callback_uzb.filter(item_name='site_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Hisob fakturasini yuklab olish")
    for image in FAKTURA_UZB:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(faktura_callback_uzb.filter(item_name='programm_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Jarayonda tez orada qo'shiladi ...")
    await call.message.delete()

# @dp.callback_query_handler(discount_callback.filter(item_name='site'))
# async def answer_question(call: CallbackQuery, callback_data:dict):
#     await call.message.reply_photo(photo="AgACAgIAAxkBAAIEQmOQh_e9biU5CkBxRRwS9Oavi1iqAAKqwTEbHAeISCwZTHOIByW8AQADAgADcwADKwQ", caption="2836123")
#     await call.message.delete()

# @dp.callback_query_handler(change_ticket_callback.filter(item_name='site'))
# async def answer_question(call: CallbackQuery, callback_data:dict):
#     await call.message.reply_photo(photo="AgACAgIAAxkBAAIEQmOQh_e9biU5CkBxRRwS9Oavi1iqAAKqwTEbHAeISCwZTHOIByW8AQADAgADcwADKwQ", caption="2836123")
#     await call.message.delete()

@dp.callback_query_handler(registration_callback_uzb.filter(item_name='site_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Web-sahifada ro'yhatdan o'tish")
    for image in REGISTRATION_UZB:
        await call.message.reply_photo(photo=image)
    await call.message.delete()

@dp.callback_query_handler(registration_callback_uzb.filter(item_name='programm_uzb'))
async def answer_question(call: CallbackQuery, callback_data:dict):
    await call.message.answer("Jarayonda tez orada qo'shiladi ...")
    await call.message.delete()