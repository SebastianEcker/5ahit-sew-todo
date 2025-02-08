from datetime import date, datetime

from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

from .category import Category

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
    category: Category
    user: 'User'
    class Config:
        orm_mode = True

