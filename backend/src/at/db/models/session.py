from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from at.db import Base
from at.db.models.user import User
from at.db.types import timestamp


# don't forget to add to __init__.py
class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True, index = True)
    token_hash: Mapped[str] = mapped_column(unique = True, index = True)
    created_at: Mapped[timestamp]
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default = text("NOW() + INTERVAL '2 weeks'"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index = True)
    user: Mapped["User"] = relationship()
    user_agent: Mapped[str | None]
    ip: Mapped[str | None]
