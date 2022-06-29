from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage #state machine
from aiogram.contrib.fsm_storage.mongo import MongoStorage #DB to save states. TODO: include this 

API_TOKEN = '5068766413:AAHQjdL3Ujx1_vtpTpMw0r5f_XTkC63rCsw'
storage = MemoryStorage()

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)
