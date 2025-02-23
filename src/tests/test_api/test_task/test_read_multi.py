from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from constants.task import TaskStatus
from models import Task

ROOT_ENDPOINT = "/task_service/api/v1/task/"


class TestReadTasks:
    async def test_read_without_filter(
        async_session: AsyncSession,
        http_client: AsyncClient,
        done_task_fixture: Task,
        failed_task_fixture: Task,
        in_progress_task_fixture: Task,
        created_task_fixture: Task,
    ) -> None:
        response = await http_client.get(ROOT_ENDPOINT)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["objects"]) == 4
        assert response_data["total"] == 4
        assert response_data["objects"][0]["id"] == done_task_fixture.id
        assert response_data["objects"][1]["id"] == failed_task_fixture.id
        assert response_data["objects"][2]["id"] == in_progress_task_fixture.id
        assert response_data["objects"][3]["id"] == created_task_fixture.id

    async def test_read_tasks_with_filter_created(
        async_session: AsyncSession,
        http_client: AsyncClient,
        done_task_fixture: Task,
        failed_task_fixture: Task,
        in_progress_task_fixture: Task,
        created_task_fixture: Task,
    ) -> None:
        params = {"status": TaskStatus.CREATED}
        response = await http_client.get(ROOT_ENDPOINT, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["objects"]) == 1
        assert response_data["total"] == 1
        assert response_data["objects"][0]["id"] == created_task_fixture.id

    async def test_read_tasks_with_filter_in_progress(
        async_session: AsyncSession,
        http_client: AsyncClient,
        done_task_fixture: Task,
        failed_task_fixture: Task,
        in_progress_task_fixture: Task,
        created_task_fixture: Task,
    ) -> None:
        params = {"status": TaskStatus.IN_PROGRESS}
        response = await http_client.get(ROOT_ENDPOINT, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["objects"]) == 1
        assert response_data["total"] == 1
        assert response_data["objects"][0]["id"] == in_progress_task_fixture.id

    async def test_read_tasks_with_filter_failed(
        async_session: AsyncSession,
        http_client: AsyncClient,
        done_task_fixture: Task,
        failed_task_fixture: Task,
        in_progress_task_fixture: Task,
        created_task_fixture: Task,
    ) -> None:
        params = {"status": TaskStatus.ERROR}
        response = await http_client.get(ROOT_ENDPOINT, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["objects"]) == 1
        assert response_data["total"] == 1
        assert response_data["objects"][0]["id"] == failed_task_fixture.id

    async def test_read_tasks_with_filter_done(
        async_session: AsyncSession,
        http_client: AsyncClient,
        done_task_fixture: Task,
        failed_task_fixture: Task,
        in_progress_task_fixture: Task,
        created_task_fixture: Task,
    ) -> None:
        params = {"status": TaskStatus.DONE}
        response = await http_client.get(ROOT_ENDPOINT, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["objects"]) == 1
        assert response_data["total"] == 1
        assert response_data["objects"][0]["id"] == done_task_fixture.id
