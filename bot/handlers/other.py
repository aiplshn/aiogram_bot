from aiogram import types, Dispatcher
from bot.create_bot import dp, bot
from bot.keyboards import keyboard_client

#Общая часть
async def echo_send(message: types.message):
    await message.answer(message.text)
    await message.reply(message.text, reply_markup = keyboard_client.kb_client)
    await bot.send_message(message.from_user.id, message.text)



def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)