from httpx import AsyncClient
from pytest_mock import MockerFixture
from sqlalchemy.ext.asyncio import AsyncSession

from crud.task import task_crud
from schemas.task import TaskCreate

ROOT_ENDPOINT = "/task_service/api/v1/task/"


class TestCreate:
    async def test_create_task(
        self,
        http_client: AsyncClient,
        async_session: AsyncSession,
        mocker: MockerFixture,
    ) -> None:
        data = TaskCreate(name="mytesttask", description="testdescription")
        mock_producer = mocker.patch("utilities.publisher.create_task")
        response = await http_client.post(
            ROOT_ENDPOINT, json=data.model_dump(exclude_unset=True)
        )
        assert response.status_code == 201
        assert mock_producer.call_count == 1
        await async_session.close()
        response_data = response.json()
        new_task = await task_crud.get_by_id(
            db=async_session, obj_id=response_data["id"]
        )
        assert mock_producer.call_args[1]["task"].id == new_task.id
