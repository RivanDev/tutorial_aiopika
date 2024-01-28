import asyncio

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage) -> None:
    print(" [x] Received message %r" % message)
    print("Message body is: %r" % message.body)

    print("Before sleep!")
    await asyncio.sleep(5)
    print("After sleep!")

async def main() -> None:
    connection = await connect("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("hello")
        await queue.consume(on_message, no_ack=True)
        print(" [x] Waiting for messages. To exit press CTRL + C")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

