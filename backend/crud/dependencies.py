from typing import Generator

from database.config import async_session
from crud.user import UserCRUD
from crud.task import TaskCRUD
from crud.category import CategoryCRUD

async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)

async def get_task_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield TaskCRUD(session)

async def get_category_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield CategoryCRUD(session)