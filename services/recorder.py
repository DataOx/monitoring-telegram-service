import time
import asyncio
import datetime

from broker import RedisClient
from db import Database
from logger import logging
from config import BROKER_POOL_TIMEOUT, TEXT_MIN_LEN


class Recorder:

    def __init__(self) -> None:
        self.redis_client = RedisClient()
        self.database = Database()
        self.logger = logging.getLogger('Recorder')

    @staticmethod
    async def register_validator(text: str) -> bool:
        return False if text.isupper() else True

    @staticmethod
    async def min_len_validator(text: str) -> bool:
        counter = len([t for t in list(text) if t.isalpha()])
        return False if counter < TEXT_MIN_LEN else True

    @staticmethod
    async def bot_status_validator(message: dict) -> bool:
        return False if message['from']['is_bot'] else True

    async def message_filter(self, message: dict) -> bool:
        text = message['text']

        is_register_valid = await self.register_validator(text=text)
        is_min_len_valid = await self.min_len_validator(text=text)
        is_not_bot = await self.bot_status_validator(message=message)

        if is_min_len_valid and is_register_valid and is_not_bot:
            return True
        return False

    async def process_message_data(self) -> None:
        datetime_now = datetime.datetime.now()
        messages = await self.redis_client.select_message_data()
        for message in messages:
            is_message_valid = await self.message_filter(message=message)

            user_id = message['from']['id']
            chat_id = message['chat']['id']
            group_name = message['chat']['title']

            if not is_message_valid:
                self.logger.info(f'Invalid message from user_id = {user_id}')

            if is_message_valid:
                self.logger.info(f'Valid message from user_id = {user_id}')

                try:
                    first_name = message['from']['first_name']
                except KeyError:
                    first_name = '-'

                try:
                    last_name = message['from']['last_name']
                except KeyError:
                    last_name = '-'

                username = message['from']['username']

                last_data = await self.database.select_last_data(user_id=user_id, chat_id=chat_id)

                if last_data:
                    last_date_activity = last_data['last_date_activity']
                    days_activity = last_data['days_activity']

                    if last_date_activity < datetime_now.date():
                        last_date_activity = datetime_now.date()
                        days_activity = last_data['days_activity'] + 1
                    else:
                        last_date_activity = last_date_activity
                        days_activity = days_activity

                    message_count = last_data['message_count'] + 1

                    await self.database.update_message_data(
                        last_date_activity=last_date_activity,
                        days_activity=days_activity,
                        message_count=message_count,
                        date_time=datetime_now,
                        user_id=user_id,
                        chat_id=chat_id
                    )
                else:
                    pass
                    await self.database.insert_message_data(
                        user_id=user_id,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        chat_id=chat_id,
                        message_count=1,
                        days_activity=1,
                        last_date_activity=datetime_now.date(),
                        date_time=datetime_now,
                        group_name=group_name
                    )

    async def main(self) -> None:
        while True:
            try:
                if self.database.connection is None:
                    await self.database.create_connection()
                await self.process_message_data()
            except Exception as exc:
                self.logger.error(exc)
                await self.database.close_connection()
                self.database.connection = None
            await asyncio.sleep(BROKER_POOL_TIMEOUT)


if __name__ == '__main__':
    time.sleep(30)
    recorder = Recorder()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(recorder.main())
    except KeyboardInterrupt:
        loop.run_until_complete(recorder.database.close_connection())

