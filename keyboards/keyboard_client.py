from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_usd = InlineKeyboardButton('USD', callback_data='set_usd')
button_rub = InlineKeyboardButton('RUB', callback_data='set_rub')

kb_client = InlineKeyboardMarkup(resize_keyboard=True)

kb_client.row(button_usd).row(button_rub)
