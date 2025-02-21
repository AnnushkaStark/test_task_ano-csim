from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_filter import FilterDepends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.database import get_async_db
from api.filters.task import TaskFilter
from crud.task import task_crud
from schemas.task import TaskCreate, TaskPaginatedResponse, TaskResponse
from services import task as task_service

router = APIRouter()


@router.get("/", response_model=TaskPaginatedResponse)
async def read_tasks(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_async_db),
    filter: TaskFilter = FilterDepends(TaskFilter),
):
    return await filter.filter(db=db, skip=skip, limit=limit)


@router.get("/{task_uid}/", response_model=TaskResponse)
async def read_task(task_uid: UUID, db: AsyncSession = Depends(get_async_db)):
    return await task_crud.get_by_uid(db=db, uid=task_uid)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(
    create_schema: TaskCreate, db: AsyncSession = Depends(get_async_db)
):
    try:
        return await task_service.create(db=db, create_data=create_schema)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
