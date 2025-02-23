from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from models import Task

ROOT_ENDPOINT = "/task_service/api/v1/task/"
