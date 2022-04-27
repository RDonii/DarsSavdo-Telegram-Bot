from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.singleInlineKeyboards import single_button
from keyboards.inline.callbacks import menu_btn
from keyboards.default.menuKeyboards import menu
from states.MenuState import Menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f'''
    Salom, {message.from_user.full_name}!
    Ushbu botimiz orqali siz dasturlash tilari hamda chet tillarini o'rganishingiz mumkin. Kurslarinmiz yuqori malakaga ega bo'lgan uxtozlar tomonidan o'tiladi derdimu ammo hozirda hech qanday darslar kontent sifatida ushbu botimizga qo'shilmagan. Chunki bu bot shunchaki bot yasashda mashg'ulot o'tqasish maqsadida qilinayapti. Ushbu matin esa joyni egallash uchun yozilgan. Shunday bo'lsa ham menu ga kirish uchun pastdagi Menu tugmasini bosishingiz mumkin.
    '''
    await message.answer(text=text, reply_markup=single_button)

@dp.callback_query_handler(menu_btn.filter(item_name='main_menu'))
async def main_menu_btn(call: types.CallbackQuery, callback_data: dict):
    await call.message.answer('Kategoriyalardan birini tanlang!', reply_markup=menu)
    await Menu.menu.set()
