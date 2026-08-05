from sqlalchemy.orm import Mapped, mapped_column

from at.db import Base


# don't forget to add to __init__.py
class Template(Base):
    __tablename__ = "IF_THIS_IS_IN_YOUR_DB_YOU_FUCKED_UP_LMAO"

    what: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
