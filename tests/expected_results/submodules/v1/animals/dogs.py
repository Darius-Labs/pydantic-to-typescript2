from pydantic import BaseModel
from enum import Enum


class DogBreed(str, Enum):
    mutt = "mutt"
    labrador = "labrador"
    golden_retriever = "golden retriever"


class Dog(BaseModel):
    name: str
    age: int
    breed: DogBreed
