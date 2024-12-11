from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.keybord import main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("s", reply_markup=main)


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("gg")


@router.message(F.text == "хуй")
async def poslan(message: Message):
    await message.answer("нет")
