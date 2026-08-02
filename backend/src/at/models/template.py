from sqlalchemy.orm import Mapped, mapped_column

from at.db import Base


# don't forget to add to __init__.py
class Table(Base):
    __tablename__ = ""

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    prop: Mapped[str] = mapped_column(nullable=False)
