import asyncio
import random
import string
import sys

from at.config import config
from at.db import Base, engine, models  # noqa: F401

target_metadata = Base.metadata


def genhash(chars: int = 4) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k = chars))

async def drop():
    if not config().devmode:
        print("this looks like a production instance!!!!")
        print("if you're really sure, turn on backend/app.config:devmode")

    hash = genhash(4)
    print("This will DROP ALL TABLES!! in the database defined under .env!!")
    print(f"type '{hash}' below to confirm:")
    conf = input()

    if conf != hash:
        print("wrong, goodbye")
        sys.exit(1)
    if input("are you sure? [y/N]").lower() != "y":
        print("no changes made")
        sys.exit(0)

    print("bye bye data oyes pog goodnight")
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.drop_all)
    print("it workied")

def entry():
    asyncio.run(drop())

if __name__ == "__main__":
    asyncio.run(drop())
