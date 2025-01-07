import logging
import random
import asyncio
from aiogram import  Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, dotenv_values

load_dotenv()
token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
unique_users = set()

@dp.message(Command("start"))
async def start_command(message: Message ):
    unique_users.add(message.from_user.id)
    count = len(unique_users)
    await message.answer(f"Привет {message.from_user.first_name}!\nНаш бот уже обслуживает {count} пользователей.")

@dp.message(Command("random"))
async def random_command(message: Message):
    name_list = ["Игорь", "Ольга", "Анна", "Алексей", "Мария"]
    await message.answer(random.choice(name_list))

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

