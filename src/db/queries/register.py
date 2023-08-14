from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.db.models import User


async def get_user_by_id(message: Message, session: sessionmaker):
    async with session() as session:
        session: AsyncSession
        user = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
        return user.one_or_none()


async def new_user(message: Message, session: sessionmaker):
    async with session() as session:
        user = User(
            telegram_id=message.from_user.id,
            username=message.from_user.username
        )
        await session.merge(user)
        await session.commit()
        return True
