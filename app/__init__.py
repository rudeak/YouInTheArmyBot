from config import API_TOKEN
from app.army_bot import ArmyBot
from app.db import db

from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from elasticsearch import Elasticsearch


es = Elasticsearch(['http://localhost:9200'])

# print ('Start build search indexses')
# from app.build_indexes import es_index
# es_index(es)
# print ('Finish build search indexses')



from app.log import *
logger.info ("Бот запущений")

inventory = ArmyBot(token=API_TOKEN)
inventory.db_connect(db)
inventory.db_create_tables()


# from app.strings.messages import create_strings
# create_strings()

# from app.keyboard.common_handlers import create_buttons
# create_buttons()

dp = Dispatcher(inventory)
dp.middleware.setup(LoggingMiddleware())

from app.commands_handlers import *
from app.inline_btn_handlers import *

# from app.jobs.passwords_jobs import delete_password
# scheduler = AsyncIOScheduler()
# scheduler.add_job(delete_password, 'interval', seconds=PASSWORD_IDLE_TIME)