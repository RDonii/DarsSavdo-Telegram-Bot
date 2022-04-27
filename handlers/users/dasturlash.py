from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from states.dasturlash import Dasturlash 
from keyboards.inline.productInlinekeyboards import productInline
from keyboards.default.pythonMenuKeyboards import pythonMenu

@dp.message_handler(Text(equals='Python darslari'), state=Dasturlash.dasturlashMenu)
async def python_menu(message: types.Message):
    await message.answer("Sohalardan birini tanlang.", reply_markup=pythonMenu)
    await Dasturlash.python.set()

@dp.message_handler(Text(equals='Delphi'), state=Dasturlash.dasturlashMenu)
async def delphi(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=productInline)
    await Dasturlash.delphi.set()

@dp.message_handler(Text(equals='Golang'), state=Dasturlash.dasturlashMenu)
async def golang(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=productInline)
    await Dasturlash.golang.set()

@dp.message_handler(Text(equals='JavaScript'), state=Dasturlash.dasturlashMenu)
async def javascript(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=productInline)
    await Dasturlash.javaScript.set()