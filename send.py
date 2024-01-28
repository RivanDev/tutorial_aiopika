import asyncio

from aio_pika import Message, connect


async def main() -> None:
    connection = await connect("amqp://guest:guest@localhost/")

    async with connection:
        channel = await connection.channel()

        queue = await channel.declare_queue("hello")

        await channel.default_exchange.publish(
            Message(b"Hello World!"),
            routing_key=queue.name,
        )

        print(" [x] Sent ' HELLO WORLD!'")

if __name__ == '__main__':
    asyncio.run(main())
