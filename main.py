
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Список уникальных пользователей (для доп. задания)
unique_users = set()

# Список имен для команды /random
names = ["Игорь", "Ольга", "Анна", "Алексей", "Мария"]

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # Считаем уникальных пользователей
    unique_users.add(user_id)
    user_count = len(unique_users)

    greeting = f"Привет, {first_name}!\nНаш бот обслуживает уже {user_count} пользователей."
    await message.reply(greeting)

# Обработчик команды /myinfo
@dp.message_handler(commands=["myinfo"])
async def myinfo_command(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username or "Не указан"

    info = (
        f"Ваш id: {user_id}\n"
        f"Ваше имя: {first_name}\n"
        f"Ваш никнейм: {username}"
    )
    await message.reply(info)

# Обработчик команды /random
@dp.message_handler(commands=["random"])
async def random_command(message: Message):
    random_name = random.choice(names)
    await message.reply(f"Случайное имя: {random_name}")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
