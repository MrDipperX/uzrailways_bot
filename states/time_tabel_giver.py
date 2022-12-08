from aiogram.dispatcher.filters.state import StatesGroup, State

class TTable(StatesGroup):
    city = State()
    city_uzb = State()
    direction = State()