from aiogram.dispatcher import FSMContext
from aiogram import types
from bot.create_bot import bot, BOT_DATA

async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    if not BOT_DATA.isAdmin(callback_query.from_user.id):
        return
    current_state = await state.get_state()
    await bot.answer_callback_query(callback_query.id)
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(callback_query.from_user.id, 'OK')