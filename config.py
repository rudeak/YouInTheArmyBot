import platform
import os
from os import environ

##################
### BOT CONFIG ###
##################
if platform.system() =='Windows':
    debug_ = True
else:
    debug_ = False

if debug_:
    API_TOKEN =  os.getenv('API_TOKEN') or  '5750210766:AAHqbBHbpXWBAemtv1axc0onpvTXKZxrrms'
    TG_LOGGER_USERS =[87017167]
if not debug_:
    API_TOKEN = os.getenv('API_TOKEN') or '5750210766:AAHqbBHbpXWBAemtv1axc0onpvTXKZxrrms'
    TG_LOGGER_USERS =[87017167]



#################
### DB CONFIG ###
#################

class Config_db():
    # MySQL
    db_name = 'roksolana'
    db_server = 'localhost'
    db_login = 'root'
    db_password = '$Fkmnfdbcnf1'
    db_prefix = '1P_'
    port = 3306
    charset = 'utf8mb4'
    debug = True
    # SQLITE
    sqlite_db = True
    sqlite_file = 'orks_must_die.db'