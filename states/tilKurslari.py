from aiogram.dispatcher.filters.state import StatesGroup, State

class TilKurslari(StatesGroup):
    tilKurslari = State()
    ingliz = State()
    rus = State()
    fransuz = State()
    koreys = State()