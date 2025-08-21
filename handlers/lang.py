from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from handlers.states import AddTx
from keyboards.langtool import lang_kb
from db import get_user_lang, set_user_lang
from i18n import t
from handlers.menu import set_owner_menu, set_user_menu
from config import OWNER_TELEGRAM_ID



router = Router()


async def re_prompt_current_step(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang") or get_user_lang(cb.from_user.id) or "uk"
    await state.update_data(lang = lang)
    cur = await state.get_state()
    if cur == AddTx.waiting_for_amount.state:
        await cb.message.edit_text(t("add_amount", lang))
    elif cur == AddTx.waiting_for_category.state:
        await cb.message.edit_text(t("ask_category", lang))
    elif cur == AddTx.waiting_for_note.state:
        await cb.message.edit_text(t("ask_note", lang))
    else:
        await cb.message.edit_text(t("hello", lang))

@router.message(Command("lang"))
async def choose_lang_cmd(message: Message):
    current =get_user_lang(message.from_user.id) or message.from_user.language_code or "uk"
    await message.answer(t("choose_lang", current), reply_markup = lang_kb())

@router.callback_query(F.data.startswith("lang:"))
async def set_lang_cb(cb: CallbackQuery, state:FSMContext):
    code = cb.data.split(":", 1)[1]
    set_user_lang(cb.from_user.id, code)
    await state.update_data(lang = code)
    await cb.answer(t("saved_lang", code, language=code))
    if cb.from_user.id == OWNER_TELEGRAM_ID:
        await set_owner_menu(cb.message.bot, cb.from_user.id, code)
    else:
        await set_user_menu(cb.message.bot, cb.from_user.id, code)
    await re_prompt_current_step(cb, state)
    