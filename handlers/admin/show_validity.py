from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
    
class FSMAdmin_ShowValidity(StatesGroup):
    username = State()

#Начало диалога показа прав. Для админа
async def start_admin_show_validity(message: types.Message):
    await FSMAdmin_ShowValidity.username.set()
    await message.reply('Введите UserName')

#Ввод UserName
async def load_username_show_validity(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
    await state.finish()
    await message.reply('Готово')