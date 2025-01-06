import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("7006515652:AAGVZlzyoypEhng2Mgakl3PuzRA_cOwJUJY")

bot = Bot(token= "7006515652:AAGVZlzyoypEhng2Mgakl3PuzRA_cOwJUJY")
dp = Dispatcher()

unique_users = set()

@dp.message(Command("start"))
async def start_command(message: Message):
    unique_users.add(message.from_user.id)
    count = len(unique_users)
    await message.answer(f"Привет, {message.from_user.first_name}! "
                         f"Наш бот уже обслуживает {count} пользователей.")

@dp.message(Command("myinfo"))
async def myinfo_command(message: Message):
    user = message.from_user
    info = f"Ваш ID: {user.id}\nВаше имя: {user.first_name}\n"
    if user.username:
        info += f"Ваш ник: @{user.username}"
    await message.answer(info)

@dp.message(Command("random"))
async def random_command(message: Message):
    names = ("Игорь", "Ольга", "Анна", "Алексей", "Мария")
    await message.answer(random.choice(names))

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())