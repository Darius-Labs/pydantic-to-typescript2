import os
import sys
from enum import Enum
from typing import List, Optional, Literal

from pydantic import BaseModel

# Make absolute imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from .schemas.schema_one import ModelOne  # noqa: F401
from .schemas.schema_two import ModelTwo  # noqa: F401
from schemas.sub_model import SubModel  # this tests absolute imports
from schemas.complex import LevelOne  # this tests absolute imports in multiple layers


class CatBreed(str, Enum):
    domestic_shorthair = "domestic shorthair"
    bengal = "bengal"
    persian = "persian"
    siamese = "siamese"


class Cat(BaseModel):
    name: str
    age: int
    declawed: bool
    breed: CatBreed


class DogBreed(str, Enum):
    mutt = "mutt"
    labrador = "labrador"
    golden_retriever = "golden retriever"


class Dog(BaseModel):
    name: str
    age: int
    breed: DogBreed


class AnimalShelter(BaseModel):
    address: str
    cats: List[Cat]
    dogs: List[Dog]
    owner: Optional[Dog]
    master: Cat


class Standalone(Enum):
    something = "something"
    anything = "anything"


class ImportedSubModule(BaseModel):
    sub: SubModel


class ComplexModelTree(BaseModel):
    one: LevelOne
