from datetime import datetime

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import DBAPIError
from fastapi import HTTPException

from auth.utils import get_password_hash
from models.category import CategoryModels
from schemas.category import Category, CategoryCreate, CategoryUpdate


class CategoryCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_category_by_id(self, id ) -> Category:
        stmt = select(CategoryModels).where(CategoryModels.id == id)
        result = await self.db_session.execute(stmt)
        category = result.scalars().first()
        if not category:
            raise HTTPException(status_code=404, detail='Category not found')
        return category

    async def get_categories(self) -> list[Category]:
        stmt = select(CategoryModels)
        result = await self.db_session.execute(stmt)
        categories = result.scalars().all()
        return categories

    async def create_category(self, category: CategoryCreate, user_id: int) -> Category:
        try:
            db_task = CategoryModels(
                name=category.name,
                color=category.color,
                user_id=user_id
            )
            self.db_session.add(db_task)
            await self.db_session.commit()
            return db_task
        except DBAPIError as e:
            await self.db_session.rollback()
            raise HTTPException(status_code=400, detail='Color is too long, only 6 characters allowed!')

    async def update_category(self, id: int, category: CategoryUpdate):
        await self.get_category_by_id(id)
        stmt = (
            update(CategoryModels)
            .where(CategoryModels.id == id)
            .values(category.model_dump())
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_category(self, id: int):
        category: Category = await self.get_category_by_id(id)
        stmt = delete(CategoryModels)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
