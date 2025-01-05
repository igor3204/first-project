import os
import asyncio
import logging
import app.mail_functions as kb
import sys

from app.handlers import router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


async def main():
    load_dotenv()
    imap = kb.connection_email()
    if not imap:
        sys.exit()

    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
