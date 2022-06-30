from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from bot.handlers.others.all_messages import *
from bot.handlers.others.start import *
from bot.handlers.others.cancel import *

def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(echo_send)

    dp.register_callback_query_handler(cancel_handler, lambda c: c.data == 'cancel', state='*')
    dp.register_callback_query_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    