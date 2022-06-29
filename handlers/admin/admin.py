from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from handlers.admin.change_access import *
from handlers.admin.change_access_add_week import *
from handlers.admin.change_access_add_month import *
from handlers.admin.show_validity import *
from handlers.admin.cancel import *

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_admin_edit_access, commands=['edit_access'], state=None)
    dp.register_message_handler(load_username, state=FSMAdmin_AccessUsers.username)
    dp.register_message_handler(load_validity, state=FSMAdmin_AccessUsers.validity)
    
    dp.register_message_handler(start_admin_edit_access_add_week, commands = ['edit_access_add_week'], state=None)
    dp.register_message_handler(load_username_add_week, state=FSMAdmin_AccessUserAddWeek.username)

    dp.register_message_handler(start_admin_edit_access_add_week, commands = ['edit_access_add_month'], state=None)
    dp.register_message_handler(load_username_add_week, state=FSMAdmin_AccessUserAddMonth.username)

    dp.register_message_handler(start_admin_show_validity, commands=['show_validity'], state=None)
    dp.register_message_handler(load_username_show_validity, state=FSMAdmin_ShowValidity.username)

    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
