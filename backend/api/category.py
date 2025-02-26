from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from auth.action import get_current_user
from crud.category import CategoryCRUD
from crud.dependencies import get_category_crud
from schemas.category import CategoryBase, Category, CategoryCreate, CategoryUpdate
from schemas.user import UserBase, User

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=list[Category], status_code=200)
async def get_categories(
    skip: int = 0, 
    limit: int = 10,
    sort_by_name: str = "asc",
    db: CategoryCRUD = Depends(get_category_crud), 
    current_user: User = Depends(get_current_user)
    ):
    return await db.get_categories(skip, limit, sort_by_name)

@router.get("/user", response_model=list[Category], status_code=200)
async def get_categories_by_user(
    skip: int = 0, 
    limit: int = 10,
    sort_by_name: str = "asc",
    db: CategoryCRUD = Depends(get_category_crud), 
    current_user: User = Depends(get_current_user)
    ):
    return await db.get_categories_by_user(current_user.id, skip, limit, sort_by_name)

@router.get("/{category_id}", response_model=Category, status_code=200)
async def get_category_by_id(category_id: int, db: CategoryCRUD = Depends(get_category_crud)):
    category = await db.get_category_by_id(category_id)
    return category

@router.post("", response_model=Category, status_code=201)
async def create_category(category: CategoryCreate, db: CategoryCRUD = Depends(get_category_crud), current_user: User = Depends(get_current_user)):
    return await db.create_category(category=category, user_id=current_user.id)

@router.put("/{category_id}", status_code=200)
async def update_category(category_id: int, category: CategoryUpdate, db: CategoryCRUD = Depends(get_category_crud), current_user: User = Depends(get_current_user)):
    return await db.update_category(id=category_id, category=category)

@router.delete("/{category_id}", status_code=204)
async def delete_category(category_id: int, db: CategoryCRUD = Depends(get_category_crud), current_user: User = Depends(get_current_user)):#
    return await db.delete_category(id=category_id)