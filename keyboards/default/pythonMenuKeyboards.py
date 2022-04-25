from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pythonMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python Backend'),
            KeyboardButton(text='Python Sun`iy Ong'),
            KeyboardButton(text='Python Ma`lumotshunos'),
        ],
        [
            KeyboardButton(text='Menu'),
        ]
    ],
    resize_keyboard=True
)