import enum

from pydantic import BaseModel


class Foo(enum.Enum):
    ONE_A = "one_a"
    ONE_B = "one_b"


class ModelOne(BaseModel):
    foo: Foo
