from datetime import date, datetime

from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import UserBase

from .category import CategoryBase

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    end_date: date
    category_id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool
    user_id: int
    category: CategoryBase | None = None
    user: 'UserBase' = None
    class Config:
        orm_mode = True

