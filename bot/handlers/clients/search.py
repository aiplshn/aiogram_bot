from aiogram import types
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.parce_data import Parce_data

async def start_client_search(message: types.Message):
    await bot.send_message(message.from_user.id, f"""Обход T+1: {Parce_data.tp1}
Фиат: {Parce_data.fiat}
Сумма: {Parce_data.sum}
Банк: {Parce_data.name_bank}
Спред: {Parce_data.spreed} - если установлен 0, то любой спред""")
    #SEARCH