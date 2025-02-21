from fastapi import APIRouter

from api.v1.endpoints.task import router as task_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(task_router, tags="/task", prefix=["Task"])
