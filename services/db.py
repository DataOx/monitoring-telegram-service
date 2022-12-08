import asyncio

import asyncpg

from config import DB_CONNECTION_URL
from logger import logging


class Database:

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.logger = logging.getLogger('Database')

    async def create_connection(self) -> None:
        self.connection = await asyncpg.connect(DB_CONNECTION_URL)
        self.logger.info('Create database connection')

    async def insert_message_data(self, user_id: int, first_name: str, last_name: str,
                                  username: str, chat_id: int, message_count: int,
                                  days_activity: int, last_date_activity: object,
                                  date_time: object, group_name: str) -> None:
        sql_command = """
            INSERT INTO api_message_info
            (user_id, chat_id, group_name, first_name, last_name, username, message_count, days_activity,
             last_date_activity, date_time)
             VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
        """

        await self.connection.execute(sql_command, user_id, chat_id, group_name, first_name,
                                      last_name, username, message_count, days_activity,
                                      last_date_activity, date_time)
        self.logger.info(f'Insert user data with id = {user_id}')

    async def update_message_data(self, last_date_activity: object, days_activity: int,
                                  message_count: int, date_time: object, user_id: int,
                                  chat_id: int):
        sql_command = """
            UPDATE api_message_info
            SET last_date_activity = $1,
            days_activity = $2,
            message_count = $3,
            date_time = $4
            WHERE user_id = $5 AND chat_id = $6
        """

        await self.connection.execute(sql_command, last_date_activity, days_activity,
                                      message_count, date_time, user_id, chat_id)
        self.logger.info(f'Update user data with id = {user_id}')

    async def select_last_data(self, user_id: int, chat_id: int):
        sql_command = """
            SELECT * FROM api_message_info WHERE user_id = $1 AND chat_id = $2;
        """
        data = await self.connection.fetchrow(sql_command, user_id, chat_id)
        return data

    async def close_connection(self):
        await self.connection.close()
        self.logger.info('Close database connection')
