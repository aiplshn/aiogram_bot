from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards import keyboard_admin
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER
import datetime

class FSMAdmin_AccessUserAddMonth(StatesGroup):
    username = State()

#Начало диалога изменения прав пользователя. Для админа
async def start_admin_edit_access_add_month(callback_query: types.CallbackQuery):
    if not BOT_DATA.isAdmin(callback_query.from_user.id):
        return
    await FSMAdmin_AccessUserAddMonth.username.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите UserName', reply_markup=keyboard_admin.kb_admins_cancel)

#Ввод UserName
async def load_username_add_month(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
        now = datetime.datetime.now()
        delta = datetime.timedelta(weeks=4)
        res = now + delta
        if BOT_CONTROLLER.changeAccessUser(res, data['username']):
            await state.finish()
            await message.reply('Готово')
        else:
            await message.reply('Не удалось, повторите попытку', reply_markup=keyboard_admin.kb_admins_cancel)
