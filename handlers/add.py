import asyncio
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db import add_tx , get_user_lang
from i18n import t
from handlers.states import AddTx
from keyboards.langtool import lang_kb


router = Router()

@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    lang = get_user_lang(message.from_user.id) or message.from_user.language_code
    await state.clear()
    await message.answer(t("cancel_", lang))

@router.message(Command("add"))
async def add_start(message: Message, state: FSMContext):
    lang = get_user_lang(message.from_user.id) or message.from_user.language_code
    await state.clear()
    await state.update_data(lang =lang)
    await state.set_state(AddTx.waiting_for_amount)
    await message.answer(t("add_amount", lang))

@router.message(AddTx.waiting_for_amount)
async def add_amount(message: Message, state:FSMContext):
    data = await state.get_data()
    lang = data.get("lang") or "uk"
    if message.text.strip().lower() == "/lang":
            await message.answer(t("choose_lang", lang), reply_markup=lang_kb())
            return
    try:
        amount = float(message.text.replace(",", "."))
    except ValueError:
        return await message.answer(t("not_a_number", lang))

    ttype = "expense" if amount < 0 else "income"
    await state.update_data(amount=abs(amount), ttype=ttype)
    await state.set_state(AddTx.waiting_for_category)
    await message.answer(t("ask_category", lang))

@router.message(AddTx.waiting_for_category)
async def add_category(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang") or "uk"
    if message.text.strip().lower() == "/lang":
            await message.answer(t("choose_lang", lang), reply_markup=lang_kb())
            return
    category = message.text.strip()
    if not category:
        return await message.answer(t("category_empty", lang))
    if len(category) > 30:
        return await message.answer(t("category_too_long",lang))
    await state.update_data(category=category)
    await state.set_state(AddTx.waiting_for_note)
    await message.answer(t("ask_note", lang))

@router.message(AddTx.waiting_for_note)
async def add_note(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang") or "uk"
    if message.text.strip().lower() == "/lang":
            await message.answer(t("choose_lang", lang), reply_markup=lang_kb())
            return
    note = message.text.strip()
    if note in {"-", "skip", "пропустити"}:
        note = None
    if note and len(note) > 200:
        return await message.answer(t("note_too_long", lang))
    
    amount = data["amount"]
    ttype = data["ttype"]
    category = data["category"]

    # запис у БД (твоя функція add_tx вже є)
    ts = await asyncio.to_thread(add_tx, message.from_user.id, amount, ttype, category, note)

    await state.clear()
    sign = "-" if ttype == "expense" else "+"
    note_part = f" — {note}" if note else ""
    await message.answer(
        t("saved_ok", 
          lang, 
          sign=sign, 
          amount=amount,   
          category=category,  
          note=note_part, 
          ts=ts[:19] 
          )
        )