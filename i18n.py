from typing import Dict

TEXTS: Dict[str,Dict[str,str]] ={
    "hello": {
        "uk": "Привіт! Використовуй /add або /list. Щоб змінити мову — /lang",
        "en": "Hi! Use /add or /list. To change language — /lang",
        "pl": "Cześć! Użyj /add lub /list. Aby zmienić język — /lang",
    },
    "choose_lang": {
        "uk": "Оберіть мову:",
        "en": "Choose your language:",
        "pl": "Wybierz język:",
    },
    "saved_lang": {
        "uk": "Мову збережено: {language}.",
        "en": "Language saved: {language}.",
        "pl": "Zapisano język: {language}.",
    },
    "no_access": {
        "uk": "🔒 Немає доступу. Твій ID: {id}",
        "en": "🔒 No access. Your ID: {id}",
        "pl": "🔒 Brak dostępu. Twój ID: {id}",
    },
    "add_amount": {
        "uk": "Введи суму (напр.: -120 або 3000). Або /cancel",
        "en": "Enter the amount (e.g. -120 or 3000). Or /cancel",
        "pl": "Podaj kwotę (np. -120 lub 3000). Lub /cancel",
    },
    "ask_category": {
        "uk": "Категорія? (напр.: кава, зарплата)",
        "en": "Category? (e.g., coffee, salary)",
        "pl": "Kategoria? (np.: kawa, pensja)",
    },
    "ask_note": {
        "uk": "Нотатка? Введи текст або '-' щоб пропустити.",
        "en": "Note? Type text or '-' to skip.",
        "pl": "Notatka? Wpisz tekst lub '-' aby pominąć.",
    },
    "saved_ok": {
        "uk": "Збережено: {sign}{amount} {category}{note} ({ts}) ✅",
        "en": "Saved: {sign}{amount} {category}{note} ({ts}) ✅",
        "pl": "Zapisano: {sign}{amount} {category}{note} ({ts}) ✅",
    },
    "not_a_number": {
        "uk": "Це не схоже на число. Спробуй ще раз, напр.: -120 або 3000.",
        "en": "This doesn't look like a number. Try again, e.g.: -120 or 3000.",
        "pl": "To nie wygląda na liczbę. Spróbuj ponownie, np.: -120 lub 3000.",
    },
    "cancel_":{
        "uk": "Скасовано. Набери /add, щоб почати заново.",
        "en": "Cancelled. Type /add to start again.",
        "pl": "Odwołane. Wpisz /add, aby zacząć od nowa.",
    },
    "category_empty": {
        "uk": "Категорія не може бути порожня. Введи ще раз.",
        "en": "Category cannot be empty. Please enter again.",
        "pl": "Kategoria nie może być pusta. Wpisz ponownie.",
    },
    "category_too_long": {
        "uk": "Категорія занадто довга (макс 30 символів).",
        "en": "Category is too long (max 30 characters).",
        "pl": "Kategoria jest za długa (maks. 30 znaków).",
    },
    "note_too_long": {
        "uk": "Нотатка занадто довга (макс 200 символів). Введи коротше або '-' щоб пропустити.",
        "en": "Note is too long (max 200 characters). Enter a shorter one or '-' to skip.",
        "pl": "Notatka jest za długa (maks. 200 znaków). Wpisz krótszą lub '-' aby pominąć.",
    },
    "no_transactions": {
        "uk": "Поки немає транзакцій.",
        "en": "No transactions yet.",
        "pl": "Na razie brak transakcji.",
    },
    "last_transactions": {
        "uk": "Останні транзакції:",
        "en": "Latest transactions:",
        "pl": "Ostatnie transakcje:",
    },
    "start": {
        "uk": "Почати",
        "en": "Start",
        "pl": "Rozpocznij"
    },
    "add": {
        "uk": "Додати транзакцію (майстер)",
        "en": "Add transaction (wizard)",
        "pl": "Dodaj transakcję (kreator)"
    },
    "list": {
        "uk": "Показати останні записи",
        "en": "Show recent entries",
        "pl": "Pokaż ostatnie wpisy"
    },
    "cancel": {
        "uk": "Скасувати діалог",
        "en": "Cancel dialog",
        "pl": "Anuluj dialog"
    },
    "lang": {
        "uk": "Вибрати мову",
        "en": "Choose language",
        "pl": "Wybierz język"
    },
    "listall": {
    "uk": "Показати записи всіх користувачів",
    "en": "Show records of all users",
    "pl": "Pokaż wpisy wszystkich użytkowników",
    }
}

def t(key: str, lang: str | None = "uk", **kwargs)-> str:
    lang = lang or "uk"
    bucket = TEXTS.get(key,{})
    msg = bucket.get(lang) or bucket.get("en") or  key
    return msg.format(**kwargs)
