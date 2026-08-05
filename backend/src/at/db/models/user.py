from datetime import date
from typing import Any

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from at.db import Base
from at.db.enums import HCAStatus, PermLevel
from at.db.types import PydanticJSONB, timestamp
from at.schemas.address import Address


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True, unique = True, index = True, autoincrement = True)
    created_at: Mapped[timestamp]
    banned: Mapped[bool] = mapped_column(default = False)
    perm_level: Mapped[PermLevel] = mapped_column(default = PermLevel.USER)
    config: Mapped[dict[str, Any]] = mapped_column(JSONB, default = dict, server_default = "{}")
        # DOCS: update(User).where(User.id == user_id).values(config=func.jsonb_set(User.config, ["key"], '"value"'))

    # info from OAuth
    hca_ok: Mapped[HCAStatus] = mapped_column(default=HCAStatus.UNVERIFIED)
    hca_id: Mapped[str] = mapped_column(unique = True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birthday: Mapped[date]
    addresses: Mapped[list[Address]] = mapped_column(PydanticJSONB(Address, is_list = True), default = list)

    # Slack API only (needs bot key)
    slack_id: Mapped[str | None]
    username: Mapped[str | None] # only from slack api
    pfp_url: Mapped[str | None]  # which sucks so probably not to be used

    # Posessions
    currency: Mapped[int] = mapped_column(default = 0)
    hours: Mapped[float] = mapped_column(default = float(0))

    # add relationships (migrate later)
