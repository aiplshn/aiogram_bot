from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_admin
from bot.create_bot import bot, BOT_DATA

class FSMAdmin_AccessUsers(StatesGroup):
    username = State()
    validity = State()

#Начало диалога изменения прав пользователя. Для админа
async def start_admin_edit_access(callback_query: types.CallbackQuery):
    if not BOT_DATA.isAdmin(callback_query.from_user.id):
        return
    await FSMAdmin_AccessUsers.username.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите UserName', reply_markup=keyboard_admin.kb_admins_cancel)

#Ввод UserName
async def load_username(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
    await FSMAdmin_AccessUsers.next()
    await message.reply('Введите срок действия', reply_markup=keyboard_admin.kb_admins_cancel)

#Ввод даты
async def load_validity(message: types.Message, state: FSMContext):
    #save date
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMAdmin_AccessUsers.next()
    # обработка 
    await state.finish()
    await message.reply('Готово')