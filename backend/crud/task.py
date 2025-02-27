from datetime import date

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.orm import joinedload
from models.task import TaskModels
from schemas.task import TaskCreate, TaskUpdate, Task, TaskBase
from fastapi import HTTPException, status
from .category import CategoryCRUD
class TaskCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_task_by_id(self, id ) -> Task:
        stmt = select(TaskModels).where(TaskModels.id == id).options(
            joinedload(TaskModels.user),
            joinedload(TaskModels.category)
        )
        result = await self.db_session.execute(stmt)
        task = result.scalars().first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return task

    async def get_tasks(self, skip: int, limit: int, category_ids: list[int], end_date: date, completed: bool, sort_by_end_date: str) -> list[Task]:
        stmt = select(TaskModels).where(TaskModels.completed == completed).offset(skip).limit(limit).options(
            joinedload(TaskModels.user),
            joinedload(TaskModels.category)
        )
        if category_ids:
            stmt = stmt.where(TaskModels.category_id.in_(category_ids))
        if end_date:
            stmt = stmt.where(TaskModels.end_date == end_date)
        if completed is not None:
            stmt = stmt.where(TaskModels.completed == completed)
        if sort_by_end_date == 'asc':
            stmt = stmt.order_by(TaskModels.end_date.asc())
        elif sort_by_end_date == 'desc':
            stmt = stmt.order_by(TaskModels.end_date.desc())

        result = await self.db_session.execute(stmt)
        tasks = result.scalars().all()
        return tasks
    
    async def get_tasks_by_user(self, user_id: int, skip: int, limit: int, category_ids: list[int], end_date: date, completed: bool, sort_by_end_date: str) -> list[Task]:
        stmt = select(TaskModels).where(TaskModels.user_id == user_id).offset(skip).limit(limit).options(
            joinedload(TaskModels.user),
            joinedload(TaskModels.category)
        )
        if category_ids:
            stmt = stmt.where(TaskModels.category_id.in_(category_ids))
        if end_date:
            stmt = stmt.where(TaskModels.end_date == end_date)
        if completed is not None:
            stmt = stmt.where(TaskModels.completed == completed)
        if sort_by_end_date == 'asc':
            stmt = stmt.order_by(TaskModels.end_date.asc())
        elif sort_by_end_date == 'desc':
            stmt = stmt.order_by(TaskModels.end_date.desc())

        result = await self.db_session.execute(stmt)
        tasks = result.scalars().all()
        return tasks

    async def create_task(self, task: TaskCreate, user_id: int) -> Task:
        await CategoryCRUD(self.db_session).get_category_by_id(task.category_id)

        task = TaskModels(
            title=task.title,
            description=task.description,
            end_date=task.end_date,
            category_id=task.category_id,
            user_id=user_id
        )
        self.db_session.add(task)
        await self.db_session.commit()
        return task

    async def update_task(self, id: int, task: TaskUpdate):
        await self.get_task_by_id(id)
        await CategoryCRUD(self.db_session).get_category_by_id(task.category_id)

        stmt = (
            update(TaskModels)
            .where(TaskModels.id == id)
            .values(task.model_dump())
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_task_completed(self, id: int):
        task: Task = await self.get_task_by_id(id)
        is_completed = True
        
        if task.completed: 
            is_completed = False
    
        stmt = (
            update(TaskModels)
            .where(TaskModels.id == id)
            .values(completed=is_completed)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_task(self, id: int):
        await self.get_task_by_id(id)

        stmt = delete(TaskModels).where(TaskModels.id == id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
