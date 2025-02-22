import uvicorn
from fastapi import FastAPI

from api.v1.router import api_router as task_service_router

app = FastAPI(
    title="TaskService",
    openapi_url="/task_service/openapi.json",
    docs_url="/task_service/docs",
)


app.include_router(task_service_router, prefix="/task_service")
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
    )
