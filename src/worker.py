import asyncio

import aio_pika
from sqlalchemy.ext.asyncio import AsyncSession

from config.configs import rabbit_settings
from utilities.task import proccess_task


async def process_message(db: AsyncSession, message: aio_pika.Message) -> None:
    await proccess_task(db=db, task_uid=message.message_id)


async def main() -> None:
    connection = await aio_pika.connect_robust(rabbit_settings.url)
    queue_name = rabbit_settings.RABBIT_QUEUE
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=100)
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    for message in queue:
        await queue.consume(process_message)
    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
