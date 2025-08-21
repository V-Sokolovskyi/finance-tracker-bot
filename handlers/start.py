from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db import get_user_lang, set_user_lang
from i18n import t
from handlers.menu import set_owner_menu, set_user_menu
from config import OWNER_TELEGRAM_ID

router = Router()

@router.message(Command("start"))
async def start(message: Message,  state: FSMContext):
    lang =get_user_lang(message.from_user.id)
    if not lang:
        lang = (message.from_user.language_code or "uk").split("-")[0]
        set_user_lang(message.from_user.id, lang)
    await state.update_data(lang = lang)
    if message.from_user.id == OWNER_TELEGRAM_ID:
        await set_owner_menu(message.bot, message.from_user.id, lang)
    else:
        await set_user_menu(message.bot, message.from_user.id, lang)
    await message.answer(t("hello", lang))


