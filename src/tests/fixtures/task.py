import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from constants.task import TaskStatus
from models import Task


@pytest_asyncio.fixture
async def created_task_fixture(async_session: AsyncSession) -> Task:
    task = Task(
        name="test_task_1",
        description="description",
        status=TaskStatus.CREATED,
    )
    async_session.add(task)
    await async_session.commit()
    await async_session.refresh(task)
    return task


@pytest_asyncio.fixture
async def in_progress_task_fixture(async_session: AsyncSession) -> Task:
    task = Task(
        name="test_task_2",
        description="description",
        status=TaskStatus.IN_PROGRESS,
    )
    async_session.add(task)
    await async_session.commit()
    await async_session.refresh(task)
    return task


@pytest_asyncio.fixture
async def failed_task_fixture(async_session: AsyncSession) -> Task:
    task = Task(
        name="test_task_3", description="description", status=TaskStatus.ERROR
    )
    async_session.add(task)
    await async_session.commit()
    await async_session.refresh(task)
    return task


@pytest_asyncio.fixture
async def done_task_fixture(async_session: AsyncSession) -> Task:
    task = Task(
        name="test_task_3", description="description", status=TaskStatus.DONE
    )
    async_session.add(task)
    await async_session.commit()
    await async_session.refresh(task)
    return task
