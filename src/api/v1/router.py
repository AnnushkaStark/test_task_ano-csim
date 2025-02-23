from fastapi import APIRouter

from api.v1.endpoints.task import router as task_router
from api.v1.endpoints.worker import router as worker_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(task_router, prefix="/task", tags=["Task"])
api_router.include_router(worker_router, prefix="/worker", tags=["Worker"])
