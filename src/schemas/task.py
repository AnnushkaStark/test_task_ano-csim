from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from constants.task import TaskStatus


class TaskBase(BaseModel):
    text: str

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
