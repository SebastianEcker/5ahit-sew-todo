from datetime import date, datetime
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    color: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True