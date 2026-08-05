import enum


class HCAStatus(enum.Enum):
    OK = "ok"
    YSWS_BAN = "ysws_ban"
    VERIFY_BAD = "verify_bad"
    UNVERIFIED = "unverified"

class PermLevel(enum.Enum):
    USER = "user"
    REVIEWER = "review"
    FULFILLER = "fulfilment"
    ADMIN = "admin"
