import logging

import aio_pika

from config.configs import rabbit_settings
from utilities.task import proccess_task


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    await proccess_task(task_id=int(message.body))


async def run_consumer() -> None:
    logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust(rabbit_settings.url)
    channel = await connection.channel()
    async with connection:
        queue_name = rabbit_settings.RABBIT_QUEUE
        await channel.set_qos(prefetch_count=100)
        queue = await channel.get_queue(queue_name)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await process_message(message=message)
