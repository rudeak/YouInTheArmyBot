from enum import unique
from peewee import *
from app.db import db, config_db
from app.log import logger
import sys
import datetime


class BaseModel(Model):

    class Meta:
        database = db
        if config_db.sqlite_db:
            pass
        else:
            table_settings = ['ENGINE=InnoDB', 'DEFAULT CHARSET=utf8']

class Orc(BaseModel):
    fio = TextField(unique=False)
    name = TextField(unique=False)
    fathername = TextField(unique=False)
    surname = TextField(unique=False)
    date_of_b = CharField(max_length=10, unique=False)
    adress = TextField(unique=False)
    passport_no = CharField(max_length=10, unique=False)
    passport_gov = TextField(unique=False)

    class Meta:
        table_name = config_db.db_prefix + 'orc'

class Geo(BaseModel):
    orc = ForeignKeyField(Orc, backref='geo_orc')
    region = TextField(unique=False, null=False)
    city = TextField(unique=False)
    adress =TextField(unique=False)

    class Meta:
        table_name = config_db.db_prefix + 'geo'

class Areas(BaseModel):
    city_type = CharField(max_length=20, unique=False)
    region_type = CharField(max_length=20, unique=False)
    region = TextField(unique=False)
    city = TextField(unique=False)

    class Meta:
        table_name = config_db.db_prefix + 'areas'

class AreaToOrc(BaseModel):
    orc = ForeignKeyField(Orc, backref='area_to_orc')
    area = ForeignKeyField(Areas, backref='area_to_orc')
    full_address = TextField(unique=False)

    class Meta:
        table_name = config_db.db_prefix + 'area_to_orc'


def create_all_tables():
        for cls in sys.modules[__name__].__dict__.values():
            try:
                if BaseModel in cls.__bases__:
                    try:
                        cls.create_table(safe=True)
                    except Exception as e:
                        if config_db.debug:
                            logger.error ('Помилка створення таблиці: '+cls._meta.table_name,  exc_info=True)
                        else:
                            logger.error ('Помилка створення таблиці: '+cls._meta.table_name)
            except Exception as e:
                pass
