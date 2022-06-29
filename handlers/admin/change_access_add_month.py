from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
    
class FSMAdmin_AccessUserAddMonth(StatesGroup):
    username = State()

#Начало диалога изменения прав пользователя. Для админа
async def start_admin_edit_access_add_month(message: types.Message):
    await FSMAdmin_AccessUserAddMonth.username.set()
    await message.reply('Введите UserName')

#Ввод UserName
async def load_username_add_month(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
    await state.finish()
    await message.reply('Готово')
