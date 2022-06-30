from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Отмена
button_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')
#Клавиатура отмена
kb_cancel = InlineKeyboardMarkup(resize_keyboard=True)
kb_cancel.row(button_cancel)