import aio_pika

from config.configs import rabbit_settings
from models import Task


async def create_task(task: Task) -> None:
    connection = await aio_pika.connect_robust(rabbit_settings.url)
    async with connection:
        channel = await connection.channel()
        routing_key = rabbit_settings.RABBIT_QUEUE
        await channel.default_exchange.publish(
            aio_pika.Message(body=str(task.id).encode()),
            routing_key=routing_key,
        )
