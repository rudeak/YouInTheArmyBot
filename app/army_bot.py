from config import *
from aiogram import Bot
from app.log import logger
from peewee import Model

class ArmyBot (Bot):
    db = None
    def db_connect (self,db):
        try:
            db.connect()
            logger.info ('Підключення до БД успішне')
            self.db = db
        except Exception as e:
            logger.critical ('Помилка підключення до бд', exc_info=True)

    def db_create_tables(self):
        import app.models as models
        if self.db !=None:
            models.create_all_tables()
        else:
            logger.error('Підключення до бази данних не здійснене')