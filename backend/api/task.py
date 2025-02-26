from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List

from auth.action import get_current_user
from crud.task import TaskCRUD
from crud.dependencies import get_task_crud
from schemas.task import TaskBase, Task, TaskCreate, TaskUpdate
from schemas.user import UserBase, User
from datetime import date

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[Task], status_code=200)
async def get_tasks(
    skip: int = 0, 
    limit: int = 10,
    category_ids: list[int] = Query(None),
    end_date: date | None = None,
    completed: bool | None = None,
    sort_by_end_date: str = Query('asc', description="Sort order: asc or desc"),
    db: TaskCRUD = Depends(get_task_crud),
    current_user: User = Depends(get_current_user)
    ):
    tasks = await db.get_tasks(skip, limit, category_ids, end_date, completed, sort_by_end_date)
    return tasks

@router.get("/user", response_model=list[Task], status_code=200)
async def get_tasks_by_user(
    skip: int = 0, 
    limit: int = 10, 
    category_ids: list[int] = Query(None),
    end_date: date | None = None,
    completed: bool | None = None,
    sort_by_end_date: str = Query('asc', description="Sort order: asc or desc"),
    db: TaskCRUD = Depends(get_task_crud), 
    current_user: User = Depends(get_current_user)
    ):
    tasks = await db.get_tasks_by_user(current_user.id, skip, limit, category_ids, end_date, completed, sort_by_end_date)
    return tasks

@router.get("/{task_id}", response_model=Task, status_code=200)
async def get_task_by_id(task_id: int, db: TaskCRUD = Depends(get_task_crud), current_user: User = Depends(get_current_user)):
    task = await db.get_task_by_id(task_id)
    return task

@router.post("", status_code=201)
async def create_task(task: TaskCreate, db: TaskCRUD = Depends(get_task_crud), current_user: User = Depends(get_current_user)):
    task = await db.create_task(task=task, user_id=current_user.id)
    return task

@router.put("/{task_id}", status_code=200)
async def update_task(task_id: int, task: TaskUpdate, db: TaskCRUD = Depends(get_task_crud), current_user: User = Depends(get_current_user)):
    return await db.update_task(id=task_id, task=task)

@router.put("completed/{task_id}", status_code=200)
async def update_task_completed(task_id: int, db: TaskCRUD = Depends(get_task_crud), current_user: User = Depends(get_current_user)):
    return await db.update_task_completed(id=task_id)

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, db: TaskCRUD = Depends(get_task_crud), current_user: User = Depends(get_current_user)):
    return await db.delete_task(id=task_id)