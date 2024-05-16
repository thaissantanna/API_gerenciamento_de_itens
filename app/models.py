from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = None
    name: str
    price: float = Field(..., gt=0, description="The price must be greater than zero")
