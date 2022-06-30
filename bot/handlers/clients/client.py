from aiogram import Dispatcher
from bot.create_bot import dp, bot, BOT_DATA

from bot.handlers.clients.set_bypass_tp1 import *
from bot.handlers.clients.set_bank_name import *
from bot.handlers.clients.set_fiat import *
from bot.handlers.clients.set_sum import *
from bot.handlers.clients.set_spreed import *
from bot.handlers.clients.search import *

def register_handler_client(dp: Dispatcher):
    #T+1
    dp.register_message_handler(start_client_set_tp1, commands=['set_tp1'], state=None)
    dp.register_callback_query_handler(client_yes_tp1, lambda c: c.data == 'yes_tp1', state=FSMClient_SetTp1.bypass_tp1)
    dp.register_callback_query_handler(client_no_tp1, lambda c: c.data == 'no_tp1', state=FSMClient_SetTp1.bypass_tp1)
    #Fiat
    dp.register_message_handler(start_client_set_fiat, commands=['set_fiat'], state=None)
    dp.register_callback_query_handler(client_set_rub, lambda c: c.data == 'set_rub', state=FSMClient_SetFiat.set_fiat)
    dp.register_callback_query_handler(client_set_usd, lambda c: c.data == 'set_usd', state=FSMClient_SetFiat.set_fiat)
    #Sum
    dp.register_message_handler(start_client_set_sum, commands=['set_bank'], state=None)
    dp.register_message_handler(client_input_sum, state=FSMClient_SetSum.set_sum)
    #Bank name
    dp.register_message_handler(start_client_set_bank_name, commands=['set_bank_name'], state=None)
    dp.register_callback_query_handler(client_set_sber, lambda c: c.data == 'set_sber', state=FSMClient_SetBankName.set_bank_name)
    dp.register_callback_query_handler(client_set_tinkoff, lambda c: c.data == 'set_tinkoff', state=FSMClient_SetBankName.set_bank_name)
    dp.register_callback_query_handler(client_set_qiwi, lambda c: c.data == 'set_qiwi', state=FSMClient_SetBankName.set_bank_name)
    dp.register_callback_query_handler(client_set_yandex_money, lambda c: c.data == 'set_yandex_money', state=FSMClient_SetBankName.set_bank_name)
    #Set spreed
    dp.register_message_handler(start_client_set_spreed, commands=['set_spreed'], state=None)
    dp.register_message_handler(client_input_spreed, state=FSMClient_SetSpreed.set_spreed)
    #Search
    dp.register_message_handler(start_client_search, commands=['search'], state=None)