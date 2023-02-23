from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.buying_ticker_state import BuyingTicket

from loader import dp, bot
from db.db import PgConn


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db_conn = PgConn()
    db_conn.add_user(message.chat.id, message.chat.username)
    await bot.send_message(chat_id=message.chat.id,
                           text="🇺🇿 Assalomu alaykum, hurmatli mijoz. Sizni qiziqtirgan masalani so'rang."
                                "\n\n🇷🇺 Здравствуйте, уважаемый клиент. Спросите что вас интересует"
                                "\n\n🇺🇿 Ассалому алайкум, хурматли мижоз. Сизние кизиктирган масалани суранг")
    await message.delete()
    await BuyingTicket.problem.set()


@dp.message_handler(CommandStart(), state=BuyingTicket.problem)
async def bot_start(message: types.Message):
    db_conn = PgConn()
    db_conn.add_user(message.chat.id, message.chat.username)
    await bot.send_message(chat_id=message.chat.id,
                           text="🇺🇿 Assalomu alaykum, hurmatli mijoz. Sizni qiziqtirgan masalani so'rang."
                                "\n\n🇷🇺 Здравствуйте, уважаемый клиент. Спросите что вас интересует"
                                "\n\n🇺🇿 Ассалому алайкум, хурматли мижоз. Сизние кизиктирган масалани суранг")
    await message.delete()
    await BuyingTicket.problem.set()



