from aiogram import Router,types
from aiogram.filters import  command

start_router = Router()
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    # message.from_user.id
    # await message.answer(f"Привет, {name}")
    await message.reply(f"Привет, {name}")