from .callbacks import menu_btn
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

single_button = InlineKeyboardMarkup(row_width=1)

main_manu = InlineKeyboardButton(text='Menu', callback_data=menu_btn.new(item_name='main_menu'))
single_button.insert(main_manu)
