import uuid

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from models import Task

ROOT_ENDPOINT = "/task_service/api/v1/task/"


class TestReadOne:
    async def test_read_success(
        self,
        http_client: AsyncClient,
        async_session: AsyncSession,
        created_task_fixture: Task,
    ) -> None:
        endpoint = f"{ROOT_ENDPOINT}{created_task_fixture.uid}/"
        response = await http_client.get(endpoint)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["name"] == created_task_fixture.name

    async def test_read_with_invalid_uid(
        self,
        http_client: AsyncClient,
        async_session: AsyncSession,
    ) -> None:
        endpoint = f"{ROOT_ENDPOINT}{uuid.uuid4()}/"
        response = await http_client.get(endpoint)
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["detail"] == "Not found"
