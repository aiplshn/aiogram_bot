from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSMAdmin_AccessUsers(StatesGroup):
    username = State()
    validity = State()

#Начало диалога изменения прав пользователя. Для админа
async def start_admin_edit_access(message: types.Message):
    await FSMAdmin_AccessUsers.username.set()
    await message.reply('Введите UserName')

#Ввод UserName
async def load_username(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
    await FSMAdmin_AccessUsers.next()
    await message.reply('Введите срок действия')

#Ввод даты
async def load_validity(message: types.Message, state: FSMContext):
    #save date
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMAdmin_AccessUsers.next()
    # обработка 
    await state.finish()
    await message.reply('Готово')