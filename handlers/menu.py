import random
from aiogram import Router, types

router = Router()

recipes = {
    "salad": {"caption": "Рецепт салата: ...", "image": "images/salad.jpg"},
    "soup": {"caption": "Рецепт супа: ...", "image": "images/soup.jpg"},
}

@router.message(commands=["recipe"])
async def send_random_recipe(message: types.Message):
    recipe = random.choice(list(recipes.values()))
    with open(recipe["image"], "rb") as photo:
        await message.answer_photo(photo=photo, caption=recipe["caption"])
