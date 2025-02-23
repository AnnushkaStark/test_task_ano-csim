from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from constants.task import TaskStatus
from schemas.paginate import PaginatedResponseBase


class TaskBase(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class TaskCreate(TaskBase):
    ...


class TaskCreateDB(TaskCreate):
    status: TaskStatus


class TaskResponse(TaskBase):
    id: int
    uid: UUID
    created_at: datetime
    status: TaskStatus


class TaskPaginatedResponse(PaginatedResponseBase):
    objects: List[TaskResponse]
