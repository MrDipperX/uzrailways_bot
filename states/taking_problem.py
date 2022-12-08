from aiogram.dispatcher.filters.state import StatesGroup, State

class ProblemData(StatesGroup):
    problem = State()
    number = State()
    answer = State()

class ProblemDataUzbek(StatesGroup):
    problem_uzb = State()
    number_uzb = State()
    answer_uzb = State()