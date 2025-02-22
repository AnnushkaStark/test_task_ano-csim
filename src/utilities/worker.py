import asyncio
import random
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from constants.task import TaskStatus
from crud.task import task_crud
from models import Task


async def proccess_task(db: AsyncSession, task_uid: UUID) -> Optional[Task]:
    if found_task := await task_crud.get_by_uid(db=db, uid=task_uid):
        progressed_task = await task_crud.update_status(
            db=db, obj=found_task, status=TaskStatus.IN_PROGRESS
        )
        await asyncio.sleep(random.randint(5, 10))
        if random.choice([True, False]):
            done_task = await task_crud.update_status(
                db=db, obj=progressed_task, status=TaskStatus.DONE
            )
            return done_task
        error_task = await task_crud.update_status(
            db=db, obj=progressed_task, status=TaskStatus.ERROR
        )
        return error_task
