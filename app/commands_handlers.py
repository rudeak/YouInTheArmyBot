from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions
from aiogram.types import ParseMode, InputFile

from app import dp, inventory
from app.log import logger
from app.keyboard.inline_keyboard import create_orc_list_keyboard


@dp.message_handler(commands=['start'], state='*')
async def start(message : types.Message,  state: FSMContext):
    telegram_id = message.chat.id
    telegram_username = message.chat.username
    text = 'Привет! Введи ФИО для подбора пакета'
    await message.answer(text,parse_mode=ParseMode().HTML, disable_web_page_preview=True)

@dp.message_handler(commands=['reindex'], state='*')
async def reindex(message : types.Message,  state: FSMContext):
    telegram_id = message.chat.id
    if telegram_id == 87017167:
        from app.build_indexes import es_index
        from app import es
        await es_index(es, inventory, telegram_id)

@dp.message_handler()
async def text_handler (message: types.Message):
        from app import es
        from config import Config_db
        from app.models import Orc
        telegram_id = message.chat.id
        index_name = Config_db.sqlite_file
        query = es.search(index = index_name, body={'query':{'multi_match': {'query': message.text, 'fields':['fio']}}})
        hits = query['hits']['hits']
        text = ''
        orc_list =[]
        for hit in hits:
            orcs = Orc.select().where(Orc.id==int(hit['_id']))
            if orcs.count()>0:
                for orc in orcs:
                    orc_list.append(orc)
        if len(orc_list)==0:
            text = 'Ничего не найдено по вашему запросу, уточните поиск!'
            await message.answer(text,parse_mode=ParseMode().HTML, disable_web_page_preview=True)
            return
        keyboard = create_orc_list_keyboard(telegram_id, orc_list)
        text = 'Вот кого я нашел:'
        await message.answer(text,reply_markup=keyboard, parse_mode=ParseMode().HTML, disable_web_page_preview=True)
        pass

