from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#Button for all users
button_usd = InlineKeyboardButton('USD', callback_data='set_usd')
button_rub = InlineKeyboardButton('RUB', callback_data='set_rub')
#Keyboard for all users
kb_client = InlineKeyboardMarkup(resize_keyboard=True)
kb_client.row(button_usd).row(button_rub)
