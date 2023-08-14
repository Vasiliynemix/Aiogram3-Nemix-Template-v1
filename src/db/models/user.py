from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models.base import Base


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=True)
