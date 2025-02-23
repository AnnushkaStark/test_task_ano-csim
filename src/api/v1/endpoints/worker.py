import asyncio

from fastapi import APIRouter

from worker import run_consumer

router = APIRouter()


@router.get("/", response_model=None)
async def start_worker():
    asyncio.create_task(run_consumer())
