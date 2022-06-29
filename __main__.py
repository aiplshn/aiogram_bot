from aiogram.utils import executor
from bot.create_bot import dp, BOT_DATA
from bot.handlers import admin, client, other
from aiogram.types import InlineKeyboardButton
from bot.handlers.admin import admin

async def on_startup(_):
    print("BOT IS STARTED")
    print('Admins:')
    for i in BOT_DATA.admins:
        print(i)
    print('Users:')
    for i in BOT_DATA.chat_ids:
        print(i)
        
admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)