from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import ParseMode, InputFile
from aiogram.utils import exceptions
import typing


from app.keyboard.buttons_def import keyb_cb
from app.keyboard.inline_keyboard import create_orc_keyboard, create_orc_list_keyboard
from app import dp, inventory
from app.models import Orc, AreaToOrc

@dp.callback_query_handler(keyb_cb.filter(type=['ORC_LIST']))
async def callback_orc_list_btn(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    await query.answer()
    id = int(callback_data['action'])
    telegram_id = query.from_user['id']
    orc = Orc.select().where(Orc.id==id).get_or_none()
    if orc == None:
        text = 'Дополнительной инофрмации нет :('
        await query.message.edit_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return
    text = '<b>ФИО: </b>'+orc.fio+'\n'
    text = text +'<b>Дата рождения: </b>'+orc.date_of_b+'\n'
    text = text + '<b>Прописка: </b>'+orc.adress+'\n'
    text = text + '<b>Номер паспорта: </b>'+orc.passport_no+'\n'
    text = text + '<b>Орган выдачи паспорта: </b>'+orc.passport_gov+'\n'
    keyboard = create_orc_keyboard(telegram_id, orc)
    await query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    pass

@dp.callback_query_handler(keyb_cb.filter(type=['ORC_KB']))
async def callback_orc_btn(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    await query.answer()
    id = int(callback_data['action'])
    telegram_id = query.from_user['id']
    orc = Orc.select().where(Orc.id==id).get_or_none()
    area = AreaToOrc.select().where(AreaToOrc.orc == orc).get_or_none()
    if area == None:
        text = 'Это бездомный орк'
        await query.message.edit_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return
    orcs = AreaToOrc.select().where(AreaToOrc.area == area.area)
    if orcs.count() > 20:
        text = 'Из населенного пункта '+area.area.city+' будет призвано '+str(orcs.count())+' чмобиков'
        await query.message.edit_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        return
    orc_lst = []
    for orc in orcs:
        orc_lst.append(orc.orc)
    keyboard = create_orc_list_keyboard(telegram_id, orc_lst)
    text = 'Из населенного пункта '+area.area.city+' будет призвано '+str(orcs.count())+' чмобиков'
    await query.message.edit_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    pass