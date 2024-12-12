import asyncio
import logging

from app.handlers import router
from aiogram import Bot, Dispatcher
from app.utils import get_config


async def main():
    config = get_config()
    token = config.get("token")
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

