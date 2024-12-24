from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from random import randint
from app.keybord import get_sizer_digs_keyboard, main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    pass
