from aiogram import Bot, Dispatcher
from  aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "7006515652:AAGVZlzyoypEhng2Mgakl3PuzRA_cOwJUJY"

bot = BOT_TOKEN(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage)