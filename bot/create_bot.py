from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #state machine
from aiogram.contrib.fsm_storage.mongo import MongoStorage #DB to save states. TODO: include this 
from bot.init_bot_data import BotInit

BOT_DATA = BotInit()
storage = MemoryStorage()

bot = Bot(BOT_DATA.token)
dp = Dispatcher(bot, storage=storage)
