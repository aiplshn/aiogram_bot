from aiogram.utils import executor
from bot.create_bot import dp, BOT_DATA, CONTROLLER_PRICE
from bot.handlers import admin
from aiogram.types import InlineKeyboardButton
from bot.handlers.admin import admin
from bot.handlers.clients import client
from bot.handlers.others import other

async def on_startup(_):
    print("BOT IS STARTED")
    print('Admins:')
    for i in BOT_DATA.admins:
        print(i)
    print('Users:')
    for i in BOT_DATA.chat_ids:
        print(i)
        
async def on_shutdown(_):
    CONTROLLER_PRICE.close_all_connections()
    print('Poka')


admin.register_handler_admin(dp)
client.register_handler_client(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)