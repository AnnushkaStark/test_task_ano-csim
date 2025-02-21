from sqlalchemy.ext.asyncio import AsyncSession

from constants.task import TaskStatus
from crud.task import task_crud
from models import Task
from schemas.task import TaskCreate, TaskCreateDB


async def create(db: AsyncSession, create_data: TaskCreate) -> Task:
    create_schema = TaskCreateDB(
        **create_data.model_dump(), status=TaskStatus.CREATED
    )
    return await task_crud.create(db=db, create_schema=create_schema)
