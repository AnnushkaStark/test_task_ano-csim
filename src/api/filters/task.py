from typing import Optional, Sequence

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from constants.task import TaskStatus
from models import Task


class TaskFilter(Filter):
    status: Optional[TaskStatus] = None

    class Constants(Filter.Constants):
        model = Task

    async def filter(
        self, db: AsyncSession, skip: int = 0, limit: int = 20
    ) -> Sequence[Task]:
        statement = (
            select(Task, func.count().over().label("total"))
            .offset(skip)
            .limit(limit)
        )
        if self.status is not None:
            statement = statement.where(Task.status == self.status)
        result = await db.execute(statement)
        rows = result.mappings().unique().all()
        return {
            "limit": limit,
            "offset": skip * limit,
            "total": rows[0]["total"] if rows else 0,
            "objects": [r["Task"] for r in rows],
        }
