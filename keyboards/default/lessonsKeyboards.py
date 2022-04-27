from turtle import width
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# lessons = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='1-dars'),
#             KeyboardButton(text='2-dars'),
#             KeyboardButton(text='3-dars'),
#         ],
#         [
#             KeyboardButton(text='4-dars'),
#             KeyboardButton(text='5-dars'),
#             KeyboardButton(text='6-dars'),
#         ],
#         [
#             KeyboardButton(text='7-dars'),
#             KeyboardButton(text='8-dars'),
#             KeyboardButton(text='9-dars'),
#         ],
#         [
#             KeyboardButton(text='Menu'),
#         ]
#     ],
#     resize_keyboard=True
# )

lessons = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

for n in range(1,10):
    lessons.insert(KeyboardButton(text=f'📕{n}-dars'))