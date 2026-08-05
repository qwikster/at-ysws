import datetime
import enum
from typing import Annotated, Any, TypeVar

from pydantic import BaseModel
from sqlalchemy import DateTime, Dialect, TypeDecorator, func
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column

T = TypeVar("T", bound=BaseModel)

# HELPERS FOR type_annotation_map
class PgEnum(SQLEnum):
    def __init__(self, enum_class: type[enum.Enum], **kw):
        db_enum_name = f"{enum_class.__name__.lower()}_enum"
        super().__init__(enum_class, name=db_enum_name, native_enum = True, **kw)


# ANNOTATED TYPES Mapped[timestamp]
timestamp = Annotated[
    datetime.datetime,
    mapped_column(DateTime(timezone=True), server_default=func.now())
]


# DATABASE TYPES mapped_column(PydanticJSONB(Address, is_list=True), default=list)
# garbage from ai    don't worry about itttt :3
class PydanticJSONB(TypeDecorator):
    impl = JSONB
    cache_ok = True

    def __init__(self, pydantic_model: type[T], is_list: bool = False):
        super().__init__()
        self.pydantic_model = pydantic_model
        self.is_list = is_list

    def process_bind_param(self, value: Any, dialect: Dialect) -> Any:
        if value is None:
            return None
        if self.is_list:
            return [
                v.model_dump() if isinstance(v, self.pydantic_model) else v
                for v in value
            ]
        return value.model_dump() if isinstance(value, self.pydantic_model) else value

    def process_result_value(self, value: Any, dialect: Dialect) -> Any:
        if value is None:
            return None
        if self.is_list:
            return [self.pydantic_model.model_validate(v) for v in value]
        return self.pydantic_model.model_validate(value)
