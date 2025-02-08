from datetime import date, datetime

from pydantic import BaseModel, EmailStr
from .category import Category
from .task import Task

# User Schema


class Base(BaseModel):
    username: str
    email: EmailStr
    birthday: date


class Register(Base):
    password: str


class Password(BaseModel):
    password: str


class Birthday(BaseModel):
    birthday: date

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    tasks: list[Task] = []
    categories: list[Category] = []
    create_time: datetime
    last_login: datetime

    class Config:
        orm_mode = True