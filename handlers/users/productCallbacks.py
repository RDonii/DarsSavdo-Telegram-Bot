from aiogram.types import CallbackQuery
from keyboards.default.lessonsKeyboards import lessons

from loader import dp

@dp.callback_query_handler(text='buy_now', state='*')
async def buy_now(call: CallbackQuery):
    await call.message.answer(text='Shu ustida ishlash kerak!')
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='buy_later', state='*')
async def buy_later(call: CallbackQuery):
    await call.answer(text="Sekin-sekin bo'lib to'larsiz, mayli.😊", show_alert=True)
    await call.message.answer(text='Yangi bilimlardan bahra oling!', reply_markup=lessons)
    await call.answer(cache_time=60)