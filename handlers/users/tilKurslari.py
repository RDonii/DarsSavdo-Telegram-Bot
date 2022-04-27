from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from states.tilKurslari import TilKurslari
from keyboards.default.lessonsKeyboards import lessons
from keyboards.inline.productInlinekeyboards import productInline

@dp.message_handler(Text(equals="Ingliz tili"), state=TilKurslari.tilKurslari)
async def lang_eng(message: types.Message):
    await message.answer('Enjoy!', reply_markup=productInline)
    await TilKurslari.ingliz.set()

@dp.message_handler(Text(equals="Rus tili"), state=TilKurslari.tilKurslari)
async def lang_ru(message: types.Message):
    await message.answer('Наслаждаться!', reply_markup=productInline)
    await TilKurslari.rus.set()

@dp.message_handler(Text(equals="Fransuz tili"), state=TilKurslari.tilKurslari)
async def lang_fr(message: types.Message):
    await message.answer('Profitez!', reply_markup=productInline)
    await TilKurslari.fransuz.set()

@dp.message_handler(Text(equals="Koreys tili"), state=TilKurslari.tilKurslari)
async def lang_kr(message: types.Message):
    await message.answer('즐기다!', reply_markup=productInline)
    await TilKurslari.koreys.set()