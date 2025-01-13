import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import logging


from handlers.start import start_router
from handlers.picture import
from handlers.bot_config import bot,dp
from handlers.menu import send_random_recipe

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

@dp.menu(Command("menu"))
async def send_menu_handler(message: types.Message):
    name = send_menu_handlerdsv.from_user.first_name
    await message.answer(f'меню {name}')


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    # message.from_user.id
    # await message.answer(f"Привет, {name}")
    await message.reply(f"Привет, {name}")


@dp.message(Command("picture"))
async def send_picture_handler(message: types.Message):
    cat_image = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=cat_image,
        caption="Умный кот"
    )


@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)
    await bot.send_message(
        chat_id=message.chat.id,
        text=txt
    )


async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
