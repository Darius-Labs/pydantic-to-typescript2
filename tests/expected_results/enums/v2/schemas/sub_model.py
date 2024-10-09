import enum

from pydantic import BaseModel


class Bar(enum.Enum):
    ONE = "one"
    TWO = "two"


class SubModel(BaseModel):
    bar: Bar
