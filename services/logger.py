import logging

logging.basicConfig(
	format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
	level='INFO',
	datefmt='%Y-%m-%d %H:%M:%S'
)

logging.getLogger('urllib3').setLevel('CRITICAL')
logging.getLogger('psycopg2').setLevel('CRITICAL')
logging.getLogger('asyncio').setLevel('CRITICAL')
logging.getLogger('aiogram').setLevel('CRITICAL')
