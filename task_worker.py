import asyncio
from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        print(f" [x] Received message {message!r}")
        await asyncio.sleep(message.body.count(b'.'))
        print(f"     Message body is: {message.body!r}")


async def main() -> None:
    connection = await connect("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("hello")
        # Declaring queue
        queue = await channel.declare_queue(
            "task_queue",
            durable=True,
        )
        await queue.consume(on_message)
        print(" [x] Waiting for messages. To exit press CTRL + C")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
