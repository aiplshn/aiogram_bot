from aiogram import types, Dispatcher
from bot.keyboards import keyboard_admin
from bot.create_bot import bot, BOT_DATA

async def command_start(message: types.Message):
    #if admin:
    if not BOT_DATA.isAdmin(message.from_user.id):
        await message.answer('СТАРТ')
    else:
        await message.answer('СТАРТ', reply_markup=keyboard_admin.kb_admins)

#Общая часть
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text, reply_markup = keyboard_client.kb_client)
    await bot.send_message(message.from_user.id, message.text)



def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(echo_send)
    