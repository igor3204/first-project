from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import random
from app.keybord import get_sizer_digs_keyboard, main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("s", reply_markup=main)


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("gg")


@router.message(F.text == "хуй")
async def poslan(message: Message):
    kb = get_sizer_digs_keyboard()
    await message.answer("нет", reply_markup=kb)


@router.message(F.text == "Отсосать")
async def suck_dick_minet(message: Message):
    await message.answer("глотай, друже, потужной минет!")


@router.callback_query(F.data == "my_dick_size")
async def get_size_my_dick(callback_data: CallbackQuery):
    dick_size = random.randint(1, 100)
    await callback_data.message.answer(f"Твой размер члена: {dick_size} см")