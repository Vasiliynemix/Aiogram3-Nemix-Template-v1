from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from src.bot.structures.fsm.register import RegisterGroup
from src.db.queries.register import new_user

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext, session: sessionmaker):
    await state.set_state(RegisterGroup.initial)
    return await message.answer('Команда Старт, для незарегестрированного пользователя')
