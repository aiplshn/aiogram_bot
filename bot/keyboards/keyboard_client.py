from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#Button for all users
#Выбор фиата
button_usd = InlineKeyboardButton('USD', callback_data='set_usd')
button_rub = InlineKeyboardButton('RUB', callback_data='set_rub')
#Обход Т+1
button_yes_tp1 = InlineKeyboardButton('Да', callback_data='yes_tp1')
button_no_tp1 = InlineKeyboardButton('Нет', callback_data='no_tp1')
#Выбор банка / кошелька
button_tinkoff = InlineKeyboardButton('Тинькофф', callback_data='set_tinkoff')
button_qiwi = InlineKeyboardButton('QIWI', callback_data='set_qiwi')
button_yandex_money = InlineKeyboardButton('ЮMoney', callback_data='set_yandex_money')
button_sber = InlineKeyboardButton('Сбербанк', callback_data='set_sber')
#Отмена
button_cancel = InlineKeyboardButton('Отмена', callback_data='cancel')

#Keyboard set fiat
kb_fiat = InlineKeyboardMarkup(resize_keyboard=True)
kb_fiat.row(button_rub).row(button_usd).row(button_cancel)
#Keyboard bypass T+1
kb_bypass_tp1 = InlineKeyboardMarkup(resize_keyboard=True)
kb_bypass_tp1.add(button_yes_tp1).add(button_no_tp1).row(button_cancel)
#Keyboard set bank name
kb_bank_name = InlineKeyboardMarkup(resize_keyboard=True)
kb_bank_name.row(button_sber).row(button_tinkoff).row(button_qiwi).row(button_yandex_money).row(button_cancel)
#Keyboard cancel
kb_client_cancel = InlineKeyboardMarkup(resize_keyboard=True)
kb_client_cancel.row(button_cancel)
