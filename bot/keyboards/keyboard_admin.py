from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#Button for admins
#изменить срок действия вручную
button_change_validity = InlineKeyboardButton('Изменить срок действия вручную', callback_data='edit_access')
#добавить неделю пользователю
button_add_week = InlineKeyboardButton('Добавить неделю', callback_data='edit_access_add_week')
#добавить месяц пользователю
button_add_month = InlineKeyboardButton('Добавить месяц', callback_data='edit_access_add_month')
#узнать срок действия пользователя
button_show_user_validity = InlineKeyboardButton('Показать срок действия', callback_data='show_validity')

#Keyboard for admins
kb_admins = InlineKeyboardMarkup(resize_keyboard=True)
kb_admins.row(button_change_validity).row(button_add_week).row(button_add_month).row(button_show_user_validity)

