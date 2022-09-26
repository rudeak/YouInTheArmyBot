from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils import exceptions

from app.keyboard.buttons_def import keyb_cb, ORC_KEYBOARD
from app.log import logger

def create_orc_list_keyboard(telegram_id, orcs):
    kb_type = 'ORC_LIST'
    result = InlineKeyboardMarkup()
    for orc in orcs:
        text = orc.fio
        try:
            inl_btn = InlineKeyboardButton(text, callback_data=keyb_cb.new(type= kb_type, action=orc.id, telegram_id=telegram_id, btn_act='orc_lst'))
        except:
            logger.error('Помилка створення клавіатури. KB_TYPE:'+kb_type+'|KB_BTN:'+orc.id+'| BTN_TEXT:'+text+'|TG_ID:'+str(telegram_id), exc_info=True)
        result.add(inl_btn)
    return result

def create_orc_keyboard(telegram_id, orc):
    kb_type = 'ORC_KB'
    result = InlineKeyboardMarkup()
    for btn in ORC_KEYBOARD:
        text = btn['text']
        try:
            inl_btn = InlineKeyboardButton(text, callback_data=keyb_cb.new(type= kb_type, action=orc.id, telegram_id=telegram_id, btn_act =btn['btn_type']))
        except:
            logger.error('Помилка створення клавіатури. KB_TYPE:'+kb_type+'|KB_BTN:'+orc.id+'| BTN_TEXT:'+text+'|TG_ID:'+str(telegram_id), exc_info=True)
        result.add(inl_btn)
    return result