from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
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
