import json
import time
import asyncio

import aioredis

from config import REDIS_CONNECTIO_URL, MESSAGE_BROKER_COUNT


class RedisClient:

    def __init__(self) -> None:
        self.connection = aioredis.from_url(url=REDIS_CONNECTIO_URL)

    async def insert_message_data(self, message: dict) -> None:
        name = f'{message["from"]["id"]}_{time.time()}'
        value = json.dumps(message)
        await self.connection.set(name=name, value=value)

    async def select_message_data(self) -> list:
        keys = await self.connection.keys()
        messages = []

        for key in keys[:MESSAGE_BROKER_COUNT]:
            message = await self.connection.get(key)
            decode_message = json.loads(message.decode())
            messages.append(decode_message)
            await self.connection.delete(key)
        await self.close_connection()

        return messages

    async def close_connection(self) -> None:
        await self.connection.close()


if __name__ == '__main__':
    redis_client = RedisClient()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(redis_client.select_message_data())
