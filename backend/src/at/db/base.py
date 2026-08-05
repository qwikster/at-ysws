from typing import ClassVar

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from typing_extensions import AsyncGenerator

from at.config import config, secret
from at.db.types import EnumResolverMap


class Base(DeclarativeBase):
    type_annotation_map: ClassVar[dict] = EnumResolverMap()

url = secret().db_url
if (url) is None:
    raise(ValueError("Databse URL is not set"))
else:
    engine = create_async_engine(url, echo = config().devmode)
async_session = async_sessionmaker(engine, expire_on_commit = False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
