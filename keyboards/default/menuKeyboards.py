from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Dasturlash'),
            KeyboardButton(text='Til Kurslari')
        ],
    ],
    resize_keyboard=True
)