import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.bot.handlers import routers
from src.configurations import conf
from src.db.database import create_async_engine, create_session_maker


async def start_bot():
    bot: Bot = Bot(token=conf.bot.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher()

    for router in routers:
        dp.include_router(router)

    engine = create_async_engine(url=conf.db.build_url())
    session = create_session_maker(engine=engine)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session=session)


if __name__ == '__main__':
    logging.basicConfig(level=conf.debug)
    asyncio.run(start_bot())
