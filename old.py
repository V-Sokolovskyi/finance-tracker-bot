from datetime import datetime, timezone
# @dp.message(Command("add"))
# async def add_cmd(message: Message):
#     # формат: /add <сума> <категорія> [нотатка]
#     try:
#         _, rest = message.text.split(" ", 1)
#         parts = rest.split()
#         amount = float(parts[0])
#         category = parts[1] if len(parts) > 1 else "misc"
#         note = " ".join(parts[2:]) if len(parts) > 2 else None
#     except Exception:
#         return await message.answer("Формат: /add <сума> <категорія> [нотатка]. Для витрати сума від'ємна.")

#     ttype = "expense" if amount < 0 else "income"
#     ts = await asyncio.to_thread(add_tx, message.from_user.id, abs(amount), ttype, category, note)
#     sign = "-" if ttype == "expense" else "+"
#     await message.answer(f"Збережено: {sign}{abs(amount)} {category} ({ts[:19]}) ✅")
a=("ksdkjsjdf","uk")
b= a[1]
print(a, b)