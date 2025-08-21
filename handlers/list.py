import asyncio
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from db import list_tx, get_user_lang
from config import OWNER_TELEGRAM_ID
from i18n import t

router = Router()


@router.message(Command("list"))
async def list_cmd(message: Message):
    lang = get_user_lang(message.from_user.id) or message.from_user.language_code
    scope_all = message.text.strip().endswith("all")
    rows = await asyncio.to_thread(
        list_tx, message.from_user.id, scope_all, 20
    )
    if not rows:
        return await message.answer(t("no_transactions",lang))
    lines = []
    for uid, amount, ttype, category, note, ts in rows:
        sign = "-" if ttype == "expense" else "+"
        owner_mark = " 👑" if OWNER_TELEGRAM_ID and uid == OWNER_TELEGRAM_ID and scope_all else ""
        note_part = f" — {note}" if note else ""
        lines.append(f"{ts[:19]} | {sign}{amount} | {category}{note_part}{owner_mark}")
    await message.answer(
        t("last_transactions",lang)+"\n" + "\n".join(lines)
                         )

@router.message(Command("listall"))
async def list_all(message:Message):
    lang = get_user_lang(message.from_user.id) or message.from_user.language_code
    rows = await asyncio.to_thread(
        list_tx, message.from_user.id, True, 20
    )
    if not rows:
        return await message.answer(t("no_transactions",lang))
    lines = []
    for uid, amount, ttype, category, note, ts in rows:
        sign = "-" if ttype == "expense" else "+"
        owner_mark = " 👑" if uid == OWNER_TELEGRAM_ID else ""
        note_part = f" — {note}" if note else ""
        lines.append(f"{ts[:19]} | {sign}{amount} | {category}{note_part}{owner_mark}")
    await message.answer(
        t("last_transactions",lang)+"\n" + "\n".join(lines)
                         )