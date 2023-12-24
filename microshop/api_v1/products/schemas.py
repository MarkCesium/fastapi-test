from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str


class Product(ProductCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
