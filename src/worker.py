import asyncio
import logging

import aio_pika
from sqlalchemy.ext.asyncio import AsyncSession

from config.configs import rabbit_settings
from utilities.task import proccess_task


async def process_message(message: aio_pika.Message) -> None:
    async with AsyncSession as session:
        await proccess_task(db=session, task_id=int(message.body))


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust(rabbit_settings.url)
    channel = await connection.channel()
    async with connection:
        queue_name = rabbit_settings.RABBIT_QUEUE
        await channel.set_qos(prefetch_count=100)
        queue = await channel.declare_queue(queue_name, auto_delete=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await process_message(message=message)
                    if queue.name in message.body.decode():
                        break


if __name__ == "__main__":
    asyncio.run(main())
