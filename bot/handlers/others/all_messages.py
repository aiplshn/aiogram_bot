from aiogram import types
from bot.create_bot import bot

async def echo_send(message: types.Message):
    await message.answer(message.text)
    await bot.send_message(message.from_user.id, message.text)