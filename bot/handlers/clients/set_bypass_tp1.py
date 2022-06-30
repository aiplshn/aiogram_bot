from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_client
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.parce_data import Parce_data

class FSMClient_SetTp1(StatesGroup):
    bypass_tp1 = State()

#Начало диалога выбора обхода блокировки Т+1
async def start_client_set_tp1(message: types.Message):
    await FSMClient_SetTp1.bypass_tp1.set()
    # await bot.answer_callback_query(callback_query.id)
    await bot.send_message(message.from_user.id, """Обходить блокировку T+1?\n
ДА - покупка совершается в разделе «Купить», продажа - через создание ордера в разделе «Купить».\n
НЕТ - покупка совершается через создание ордера в разделе «Продать», продажа - через создание ордера в разделе «Купить».""",
reply_markup=keyboard_client.kb_bypass_tp1)

#Выбор да
# async def client_set_tp1(message: types.Message, state: FSMContext):
async def client_yes_tp1(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено YES')
    Parce_data.tp1 = True
    await state.finish()
    

#Выбор нет
# async def client_set_tp1(message: types.Message, state: FSMContext):
async def client_no_tp1(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Установлено NO')
    Parce_data.tp1 = False
    await state.finish()