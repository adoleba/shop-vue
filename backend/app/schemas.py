from typing import Any

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class Product(BaseModel):
    producer: str
    name: str
    description: str
    category: str
    memory: str
    screen: str
    price: int
    processor: str
    disk: str
    onStock: bool
    img_url: str

    class Config:
        orm_mode = True
