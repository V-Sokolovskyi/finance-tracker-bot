import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats
from i18n import t
from handlers.lang import router as lang_router
from handlers.add import router as add_router
from handlers.list import router as list_router
from handlers.start import router as start_router
from config import TOKEN
from handlers.menu import build_commands




if not TOKEN:
    raise RuntimeError("No TELEGRAM_BOT_TOKEN in .env")

bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_routers(
    add_router,
    list_router, 
    lang_router,
    start_router
    )


# ---------- Handlers ----------


async def main():
    await bot.set_my_commands(build_commands("uk"),
                              scope=BotCommandScopeAllPrivateChats())
    
   
    print("Бот запущений. Ctrl+C щоб зупинити.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())