from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dasturlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python darslari'),
            KeyboardButton(text='Golang'),
            KeyboardButton(text='JavaScript'),
            KeyboardButton(text='Delphi'),
        ],
        [
            KeyboardButton(text='Menu')
        ]
    ],
    resize_keyboard=True
)