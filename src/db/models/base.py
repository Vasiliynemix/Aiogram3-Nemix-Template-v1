from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __tablename__: str

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, nullable=False, unique=True)
