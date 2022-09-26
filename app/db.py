from config import Config_db
from peewee import *
from playhouse.shortcuts import ReconnectMixin

config_db = Config_db()
if config_db.sqlite_db:
	class MyRetryDB(ReconnectMixin, SqliteDatabase):
		pass
else:
	class MyRetryDB(ReconnectMixin, MySQLDatabase):
		pass


# Database connection
if config_db.sqlite_db:
	db = MyRetryDB(config_db.sqlite_file)
	# db.register_fields({'primary_key': 'INTEGER AUTOINCREMENT'})
else:
	db = MyRetryDB(config_db.db_name, user=config_db.db_login, password=config_db.db_password,host=config_db.db_server, port=config_db.port, charset=config_db.charset)
	# db.register_fields({'primary_key': 'INTEGER AUTOINCREMENT'})

