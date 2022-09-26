import logging
import logging.handlers
import os
from config import *

if not os.path.exists("log"):
    os.makedirs("log")

# Configure logging
log_file_name = 'log/bot.log'
logging_level = logging.INFO

logging.getLogger('apscheduler.executors.default').setLevel(logging.ERROR)
logging.getLogger('apscheduler.scheduler').setLevel(logging.ERROR)
logging.getLogger('aiogram.dispatcher.dispatcher').setLevel(logging.ERROR)
logging.getLogger('aiogram').setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler = logging.handlers.TimedRotatingFileHandler(log_file_name, when="midnight", backupCount=10, encoding='utf-8' )
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging_level)
