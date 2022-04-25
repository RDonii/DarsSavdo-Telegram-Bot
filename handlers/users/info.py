from aiogram import types

from loader import dp

@dp.message_handler(commands="info")
async def bot_info(message: types.Message):
    await message.answer('Ushbu bot mohirdev.uz sahifasida joylashgan "Mukammal telegram bot" darslar to`plami o`quvchisining mashg`ulot o`tqazish boti. Admin bilan @RajabovDoniyorbek manzili orqali bog`lanishingiz mumkin.')