import time

from aiogram import Bot, Dispatcher, executor, types

from config import TELEGRAM_BOT_API_TOKEN
from broker import RedisClient
from logger import logging


class MonitoringBot:

    def __init__(self) -> None:
        self.bot = Bot(token=TELEGRAM_BOT_API_TOKEN)
        self.dispatcher = Dispatcher(self.bot)
        self.redis_client = RedisClient()
        self.logger = logging.getLogger('Monitoring Bot')
        self.dispatcher.register_message_handler(callback=self.text_message_collector)

    async def text_message_collector(self, message: types.Message) -> None:
        if message['chat']['id'] > 0:
            await message.answer('Sorry! I only work with groups!')
        else:
            await self.redis_client.insert_message_data(message=dict(message))
            log_message = f'Push message to broker from user with id = {message["from"]["id"]}'
            self.logger.info(log_message)


if __name__ == '__main__':
    time.sleep(30)
    monitoring_bot = MonitoringBot()
    executor.start_polling(monitoring_bot.dispatcher)
