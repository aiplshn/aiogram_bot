from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_client
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.client import Parce_data

class FSMClient_SetBankName(StatesGroup):
    set_bank_name = State()

#Начало диалога выбора банка
async def start_client_set_bank_name(message: types.Message):
    await FSMClient_SetBankName.set_bank_name.set()
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(message.from_user.id, "Выберите банк/кошелёк", reply_markup=keyboard_client.kb_bank_name)

#Выбор sber
async def client_set_sber(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено S')
    Parce_data.name_bank = 'Сбербанк'
    await state.finish()
    
#Выбор tinkoff
async def client_set_tinkoff(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено T')
    Parce_data.name_bank = 'Тинькофф'
    await state.finish()
    
#Выбор qiwi
async def client_set_qiwi(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено Q')
    Parce_data.name_bank = 'QIWI'
    await state.finish()

#Выбор yandex money
async def client_set_yandex_money(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено YM')
    Parce_data.name_bank = 'ЮMoney'
    await state.finish()
    