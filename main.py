import os
import asyncio
import logging
import sys
import functions
import config

from app.handlers import router
from aiogram import Bot, Dispatcher


async def get_mail_letter():
    imap = functions.connection_email()
    if not imap:
        sys.exit()
    else:
        functions.get_topic()


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
