import asyncio
import sys

from aio_pika import Message, connect, DeliveryMode


async def main() -> None:
    # Perform connection
    connection = await connect("amqp://guest:guest@localhost/")

    async with (connection):
        # Creating a channel
        channel = await connection.channel()

        message_body = b" ".join(
             arg.encode() for arg in sys.argv[1:]
         ) or b"Hello World!"

        message = Message(
            message_body, delivery_mode=DeliveryMode.PERSISTENT,
        )
        # Sending the message
        await channel.default_exchange.publish(
            message, routing_key="task_queue",
        )

        print(f" [x] Sent {message_body!r}")

if __name__ == '__main__':
    asyncio.run(main())
