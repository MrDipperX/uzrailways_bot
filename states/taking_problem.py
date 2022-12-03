from aiogram.dispatcher.filters.state import StatesGroup, State

class ProblemData(StatesGroup):
    problem = State()
    number = State()