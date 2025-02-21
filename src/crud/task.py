from typing import Optional
from uuid import UUID

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from constants.task import TaskStatus
from models import Task
from schemas.task import TaskCreateDB


class TaskCDUD:
    async def get_by_uid(self, db: AsyncSession, uid: UUID) -> Optional[Task]:
        statement = select(Task).where(Task.uid == uid)
        result = await db.execute(statement)
        return result.scalars().first()

    async def create(
        db: AsyncSession, create_schema: TaskCreateDB, commit: bool = True
    ) -> Task:
        data = create_schema.model_dump(exclude_unset=True)
        stmt = insert(Task).values(**data).returning(Task)
        res = await db.execute(stmt)
        obj = res.scalars().first()
        if commit:
            await db.commit()
            await db.refresh(obj)
        return obj

    async def update_status(
        self, db: AsyncSession, obj: Task, status: TaskStatus
    ) -> Task:
        obj.status = status
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj


task_crud = TaskCDUD()
