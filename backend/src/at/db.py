from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from at.config import get_config


class Base(DeclarativeBase):
    pass

engine = create_async_engine(get_config()["db_url"], echo = get_config()["devmode"])
