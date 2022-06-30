from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_client
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.client import Parce_data

class FSMClient_SetFiat(StatesGroup):
    set_fiat = State()

#Начало диалога выбора фиата
async def start_client_set_fiat(message: types.Message):
    await FSMClient_SetFiat.set_fiat.set()
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(message.from_user.id, "Выберите валюту", reply_markup=keyboard_client.kb_fiat)

#Выбор rub
async def client_set_rub(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено R')
    Parce_data.fiat = 'RUB'
    await state.finish()
    
#Выбор usd
async def client_set_usd(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено U')
    Parce_data.fiat = 'USD'
    await state.finish()

    