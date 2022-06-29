from aiogram import types, Dispatcher
from keyboards import keyboard_client
from keyboards import keyboard_admin
from bot.create_bot import dp, bot, BOT_DATA

#Клиентская часть
#**************************************** Обработка сообщений от пользователя ****************************************
async def command_start(message: types.message):
    #if admin:
    if not BOT_DATA.isAdmin(message.from_user.id):
        await message.answer('СТАРТ')
    else:
        await message.answer('СТАРТ', reply_markup=keyboard_admin.kb_admins)

#**************************************** Обработка события нажатия на inline кнопку  ****************************************

async def process_callback_button_set_usd(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id) #Чтобы пользователь не ожидал ответа (крутятся часики)
    await bot.send_message(callback_query.from_user.id, f"Нажата первая кнопка! {callback_query.data}")

async def process_callback_button_set_rub(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id) #Чтобы пользователь не ожидал ответа (крутятся часики)
    await bot.send_message(callback_query.from_user.id, f"Нажата вторая кнопка! {callback_query.data}")

#**************************************** Регистрация обработок  ****************************************

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_callback_query_handler(process_callback_button_set_usd, lambda c: c.data == 'set_usd')
    dp.register_callback_query_handler(process_callback_button_set_rub, lambda c: c.data == 'set_rub')