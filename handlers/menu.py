from aiogram.types import BotCommand, BotCommandScopeChat
from i18n import t

def build_commands(lang: str) -> list[BotCommand]:
    return [
        BotCommand(command="start",  description=t("start",  lang)),   
        BotCommand(command="add",    description=t("add",    lang)),   
        BotCommand(command="list",   description=t("list",   lang)),   
        BotCommand(command="cancel", description=t("cancel", lang)),   
        BotCommand(command="lang",   description=t("lang",   lang)),   
    ]
def build_commands_owner(lang: str) -> list[BotCommand]:
    return [
        BotCommand(command="listall", description= t("listall", lang)) 
    ]

async def set_user_menu(bot, user_id: int, lang: str):
    await bot.set_my_commands(build_commands(lang), scope=BotCommandScopeChat(chat_id= user_id))

async def set_owner_menu(bot, user_id: int, lang: str):
    await bot.set_my_commands(build_commands(lang) + build_commands_owner(lang),
                              scope=BotCommandScopeChat(chat_id=user_id))