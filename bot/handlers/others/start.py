from aiogram import types
from bot.keyboards import keyboard_admin
from bot.create_bot import BOT_DATA, BOT_CONTROLLER

async def command_start(message: types.Message):
    #if admin:
    print(f"Пользователь {message.from_user.username} нажал на старт")
    if not BOT_DATA.isAdmin(message.from_user.id):
        await message.answer('СТАРТ')
        BOT_CONTROLLER.trialAccessForUser(message.from_user.username, message.from_user.id)
    else:
        await message.answer('СТАРТ', reply_markup=keyboard_admin.kb_admins)