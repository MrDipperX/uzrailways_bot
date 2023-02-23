from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_command
from db.db import PgConn


async def on_startup(dispatcher):
    await set_default_command(dispatcher)
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    db_conn = PgConn()
    db_conn.create_tables()
    db_conn.auto_insert_qa()

    executor.start_polling(dp, on_startup=on_startup)
