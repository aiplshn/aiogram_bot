from aiogram import types
from bot.create_bot import bot, BOT_DATA, BOT_CONTROLLER, CONTROLLER_PRICE
from bot.handlers.clients.parce_data import Parce_data
from parse_best_change.sources import banks, find_bundle
import time

async def getParseData(chat_id, fiat, name_bank, spreed, sum, tp1):
    id = CONTROLLER_PRICE.newConnection()
    name_bank = banks.get_banks_binance_from_bc(name_bank)
    bundles_str = find_bundle.FindAllBundles(CONTROLLER_PRICE, (float)(sum), fiat, name_bank, tp1, (float)(spreed), id_connection=id)
    count = 0
    for i in bundles_str:
        for j in i:
            if j != '':
                count += 1
            await bot.send_message(chat_id, j)
            time.sleep(0.1)
    if count != 0:
        await bot.send_message(chat_id, f"Всего {count} связок")
    else:
        await bot.send_message(chat_id, 'Не найдено, попробуйте изменить параметры')
    CONTROLLER_PRICE.closeConnection(id=id)

async def start_client_search(message: types.Message):
    if BOT_CONTROLLER.getAccessUser(id=message.from_user.id) or BOT_CONTROLLER.isAdmin(id=message.from_user.id):

        await bot.send_message(message.from_user.id, f"""Обход T+1: {Parce_data.tp1}
Фиат: {Parce_data.fiat}
Сумма: {Parce_data.sum}
Банк: {Parce_data.name_bank}
Спред: {Parce_data.spreed}""")
        await getParseData(message.from_user.id, Parce_data.fiat, Parce_data.name_bank, Parce_data.spreed, Parce_data.sum, Parce_data.tp1)
    else:
        await bot.send_message(message.from_user.id, 'К сожалению, у вас нет прав доступа. Обратитесь к админу.')
    #SEARCH