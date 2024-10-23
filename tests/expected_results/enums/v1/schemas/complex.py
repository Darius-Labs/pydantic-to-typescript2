from enum import Enum

from pydantic import BaseModel


class EnumLevelThree(str, Enum):
    SOMETHING = "something"
    SOMETHING_ELSE = "something_else"
    ANOTHER_THING = "another_thing"


class LevelTwoData(BaseModel):
    three: EnumLevelThree


class LevelTwo(BaseModel):
    data: LevelTwoData


class LevelOne(LevelTwo):
    something: int
