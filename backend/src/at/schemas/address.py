from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str # addr!yLAuOZ
    primary: bool = False
    first_name: str
    last_name: str
    line_1: str
    line_2: str | None = None
    city: str
    state: str
    postal_code: str
    country: str
    phone: str | None = None
