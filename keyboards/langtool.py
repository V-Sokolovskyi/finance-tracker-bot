from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

LANGS = [("Українська", "uk"), ("English", "en"), ("Polski", "pl")]


def lang_kb() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=name, callback_data=f"lang:{code}")] 
                         for name, code in LANGS
        ]
    return InlineKeyboardMarkup(inline_keyboard=rows)    
