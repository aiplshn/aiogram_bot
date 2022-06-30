from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot.keyboards.keyboard_other import kb_cancel
from bot.create_bot import bot, BOT_DATA
from bot.create_bot import BOT_CONTROLLER
import datetime

class FSMAdmin_AccessUsers(StatesGroup):
    username = State()
    validity = State()

#Начало диалога изменения прав пользователя. Для админа
async def start_admin_edit_access(callback_query: types.CallbackQuery):
    if not BOT_DATA.isAdmin(callback_query.from_user.id):
        return
    await FSMAdmin_AccessUsers.username.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите UserName', reply_markup=kb_cancel)

#Ввод UserName
async def load_username(message: types.Message, state: FSMContext):
    #save username
    async with state.proxy() as data: #state.proxy - словарь хранения инфы. 
        data['username'] = message.text
    await FSMAdmin_AccessUsers.next()
    await message.reply('Введите срок действия в формате dd.mm.YYYY HH:MM', reply_markup=kb_cancel)

#Ввод даты
async def load_validity(message: types.Message, state: FSMContext):
    #save date
    async with state.proxy() as data:
        data['date'] = message.text
    # await FSMAdmin_AccessUsers.next()
    # обработка
    async with state.proxy() as data:
        try:
            dt = datetime.datetime.strptime(data['date'], '%d.%m.%Y %H:%M')
            if BOT_CONTROLLER.changeAccessUser(dt, data['username']):
                await message.reply('Готово')
                await state.finish()
        except Exception as e:
            await message.reply('Не удалось, повторите попытку', reply_markup=kb_cancel)
            return
        # BOT_CONTROLLER.changeAccessUser()
    # await message.reply('Готово')