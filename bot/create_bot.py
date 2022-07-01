from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #state machine
from aiogram.contrib.fsm_storage.mongo import MongoStorage #DB to save states. TODO: include this 
from bot.init_bot_data import BotInit
from bot.bot_controller import BotController
from parse_best_change.sources.controller_prices import ControllerPrices

BOT_DATA = BotInit()
storage = MemoryStorage()
bot = Bot(BOT_DATA.token)
dp = Dispatcher(bot, storage=storage)
BOT_CONTROLLER = BotController(BOT_DATA, bot)
CONTROLLER_PRICE = ControllerPrices()
