from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from bot.handlers.admin.change_access import *
from bot.handlers.admin.change_access_add_week import *
from bot.handlers.admin.change_access_add_month import *
from bot.handlers.admin.show_validity import *
from bot.handlers.admin.cancel import *

def register_handler_admin(dp: Dispatcher):
    dp.register_callback_query_handler(start_admin_edit_access, lambda c: c.data == 'edit_access', state=None)
    dp.register_message_handler(load_username, state=FSMAdmin_AccessUsers.username)
    dp.register_message_handler(load_validity, state=FSMAdmin_AccessUsers.validity)

    dp.register_callback_query_handler(start_admin_edit_access_add_week, lambda c: c.data == 'edit_access_add_week', state=None)
    dp.register_message_handler(load_username_add_week, state=FSMAdmin_AccessUserAddWeek.username)

    dp.register_callback_query_handler(start_admin_edit_access_add_month, lambda c: c.data == 'edit_access_add_month', state=None)
    dp.register_message_handler(load_username_add_month, state=FSMAdmin_AccessUserAddMonth.username)

    dp.register_callback_query_handler(start_admin_show_validity, lambda c: c.data == 'show_validity', state=None)
    dp.register_message_handler(load_username_show_validity, state=FSMAdmin_ShowValidity.username)

    dp.register_callback_query_handler(cancel_handler, lambda c: c.data == 'cancel', state='*')
    dp.register_callback_query_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
