from aiogram import types
from bot.keyboards import keyboard_admin
from bot.create_bot import BOT_DATA

async def command_start(message: types.Message):
    #if admin:
    if not BOT_DATA.isAdmin(message.from_user.id):
        await message.answer('СТАРТ')
    else:
        await message.answer('СТАРТ', reply_markup=keyboard_admin.kb_admins)