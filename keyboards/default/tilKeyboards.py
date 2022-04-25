from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tilKurslari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ingliz tili'),
            KeyboardButton(text='Rus tili'),
            KeyboardButton(text='Fransuz tili'),
            KeyboardButton(text='Koreys tili'),
        ],
        [
            KeyboardButton(text='Menu'),
        ]
    ],
    resize_keyboard=True
)