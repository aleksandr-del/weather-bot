#!/usr/bin/env python3


from logger import logging_config
import logging
import logging.config
from config.config import Config, load_config
from handlers import user
from filters.filter import UserFilter
from aiogram import Bot, Dispatcher
import asyncio


logging.config.dictConfig(logging_config)
logger = logging.getLogger("logger")
config: Config = load_config("./.env")
bot = Bot(config.bot.token)
dp = Dispatcher()
dp.message.filter(UserFilter(config.bot.user_ids))
dp.include_routers(user.router)


async def main(logger: logging.Logger = logger, bot: Bot = bot, dp: Dispatcher = dp):
    logger.info("Starting a Telegram bot ...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
