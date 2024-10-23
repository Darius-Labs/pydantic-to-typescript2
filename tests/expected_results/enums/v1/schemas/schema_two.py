import enum

from pydantic import BaseModel


class Foo(enum.Enum):
    TWO_A = "two_a"
    TWO_B = "two_b"


class ModelTwo(BaseModel):
    foo: Foo
