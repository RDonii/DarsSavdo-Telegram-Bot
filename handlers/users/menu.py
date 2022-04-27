from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from states.MenuState import Menu
from states.dasturlash import Dasturlash 
from states.tilKurslari import TilKurslari
from keyboards.default.dasturlashKeyboards import dasturlash
from keyboards.default.tilKeyboards import tilKurslari
from keyboards.default.menuKeyboards import menu


@dp.message_handler(Text(equals='Menu'), state='*')
async def main_menu(message: types.Message):
    await message.answer('Kategoriyalardan birini tanlang!', reply_markup=menu)
    await Menu.menu.set()

@dp.message_handler(Text(equals='Dasturlash'), state=Menu.menu)
async def coding_menu(message: types.Message):
    await message.answer('Dasturlash tillaridan birini tanlang!', reply_markup=dasturlash)
    await Dasturlash.dasturlashMenu.set()

@dp.message_handler(Text(equals='Til Kurslari'), state=Menu.menu)
async def lang_menu(message: types.Message):
    await message.answer("Chet tillaridan birini tanlang.", reply_markup=tilKurslari)
    await TilKurslari.tilKurslari.set()