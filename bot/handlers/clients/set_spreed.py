from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_client
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
from bot.handlers.clients.parce_data import Parce_data

class FSMClient_SetSpreed(StatesGroup):
    set_spreed = State()

#Начало диалога ввода спреда
async def start_client_set_spreed(message: types.Message):
    await FSMClient_SetSpreed.set_spreed.set()
    await bot.send_message(message.from_user.id, "Введите спред", reply_markup=keyboard_client.kb_client_cancel)

#Ввод спреда
async def client_input_spreed(message: types.Message, state: FSMContext):
    try:
        if (float)(message.text) > 0:
            await message.reply('Готово ' + message.text)
            Parce_data.spreed = message.text
            await state.finish()
        else:
            await message.reply('Введите положительное число')
    except Exception as e:
        await message.reply('Не удалось, повторите попытку')


    