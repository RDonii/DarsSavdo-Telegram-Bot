from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp
from states.dasturlash import Dasturlash
from keyboards.default.lessonsKeyboards import lessons

@dp.message_handler(Text(equals="Python Backend"), state=Dasturlash.python)
async def python_backend(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=lessons)
    await Dasturlash.pythonBackend.set()

@dp.message_handler(Text(equals="Python Sun`iy Ong"), state=Dasturlash.python)
async def python_AI(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=lessons)
    await Dasturlash.pythonAI.set()

@dp.message_handler(Text(equals="Python Ma`lumotshunos"), state=Dasturlash.python)
async def python_backend(message: types.Message):
    await message.answer('Yangi bilimlardan bahra oling!', reply_markup=lessons)
    await Dasturlash.pythonDS.set()