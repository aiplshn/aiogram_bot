from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_client
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.parce_data import Parce_data

class FSMClient_SetSum(StatesGroup):
    set_sum = State()

#Начало диалога ввода суммы
async def start_client_set_sum(message: types.Message):
    await FSMClient_SetSum.set_sum.set()
    await bot.send_message(message.from_user.id, "Введите сумму", reply_markup=keyboard_client.kb_client_cancel)

#Ввод суммы
async def client_input_sum(message: types.Message, state: FSMContext):
    try:
        if (float)(message.text) > 0:
            Parce_data.sum = message.text
            await state.finish()
            await message.reply('Готово ' + message.text)
        else:
            await message.reply('Введите положительное число')
    except Exception as e:
        await message.reply('Не удалось, повторите попытку')

    