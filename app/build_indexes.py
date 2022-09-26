from config import Config_db
from app.models import Orc


async def es_index(es, bot=None, telegram_id=None):
    index_name = Config_db.sqlite_file
    doc_type = '_doc'
    orcs = Orc.select()
    i = 0
    if bot and telegram_id:
        text = 'Побудова індексу пошуку розпочата'
        await bot.send_message(telegram_id,text)
    for p in orcs:
        s = es.index(index = index_name, id = p.id, body = {
                    'fio': p.fio})
        text = str(p.id)+'. '+p.fio
        print (text)
        i = i + 1
        if bot and telegram_id and i == 10:
            await bot.send_message(telegram_id,text)
            i = 0
    if bot and telegram_id:
        text = 'Побудова індексу пошуку заверешена'
        await bot.send_message(telegram_id,text)


def es_index_sync(es):
    index_name = Config_db.sqlite_file
    doc_type = '_doc'
    orcs = Orc.select()
    for p in orcs:
        s = es.index(index = index_name, id = p.id, body = {
                    'fio': p.fio})
        text = str(p.id)+'. '+p.fio
        print (text)