# Finance Tracker Bot
🤖A simple Telegram bot for personal finance tracking.
Add expenses and incomes, categorize transactions, leave notes, and view your history.
Multilingual (UA/EN/PL) with per-chat command menus.🗺

---

## ✨ Features
- Add transactions via a guided wizard (`/add`): amount → category → note.
- Income & expense detection (negative = expense, positive = income).
- List recent transactions (`/list`); optional owner-only command (`/listall`).
- Multilingual UX: Ukrainian, English, Polish. Users pick `/lang`; choice is remembered.
- Per-chat command menu localized to the user’s language.
- SQLite storage out of the box; easy to swap for Postgres later.
- aiogram v3 & FSM for clean, modular handlers.
  
---

## Table of Contents
1. [Installation](#-installation)
2. [Environment variables](#-environment-variables)
3. [Project structure](#project-structure)
4. [Running (polling)](#-running-polling)
5. [Commands (user)](#-commands-user)
6. [Data model (SQLite)](#-data-model-sqlite)
7. [Internationalization (i18n)](#-internationalization-i18n)
8. [Roadmap](#-roadmap)
9. [License](#license)

---
<a id="installation"></a>
## 🧰 Installation

```bash
git clone https://github.com/V-Sokolovskyi/finance-tracker-bot
cd finance-tracker-bot

python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🔐 Environment variables
```bash

# Telegram
TELEGRAM_BOT_TOKEN=1234567890:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
OWNER_TELEGRAM_ID=123456789
# Database (SQLite by default)
DATABASE_URL =

```

---
<a id="project-structure"></a>
## 🗂️ Project structure 
```bash

finance-tracker-bot/
├─ bot.py
├─ config.py
├─ db.py
├─ i18n.py
├─ handlers/
│  ├─ add.py
│  ├─ lang.py
│  ├─ list.py
│  ├─ menu.py
│  ├─ start.py
│  ├─ states.py
│  └─ __init__.py
├─ keyboards/
│  ├─ langtool.py
│  └─ __init__.py
├─ requirements.txt
├─ .env.example
├─ .gitignore
└─ LICENSE

```

---

## ▶ Running (polling)
```bash

python bot.py

```
- Tables are created automatically on first run.
- Bot uses long polling locally.

---

## 💬 Commands (user)

| Command    | What it does                                                |
|------------|-------------------------------------------------------------|
|  `/start`	 | Welcome + sets your language (from DB / Telegram / default).|
|  `/add`	   | Start the add-transaction wizard (amount → category → note).|
|  `/list`	 | Show your recent transactions.                              |
|  `/lang`	 | Choose language (UA/EN/PL); remembered for your chat.       |
|  `/cancel` | Cancel current dialog.                                      |

### Owner-only (optional):

| Command    | What it does                                                |
|------------|-------------------------------------------------------------|
| `/listall` |Show recent transactions across all users                    |

Owner/whitelist checks are based on Telegram IDs.

---

## 🗃 Data model (SQLite)

- users: `telegram_id (PK), lang`
- transactions:
`id (PK), user_id, amount (REAL),
ttype ('income' | 'expense'), category, note, ts (ISO string)`

All DB access uses parameterized queries to avoid SQL injection.

---

## 🌐 Internationalization (i18n) 

- Texts live in i18n.py as a dictionary, e.g.:
  ```bash
  TEXTS = {
    "hello": { "uk": "...", "en": "...", "pl": "..." },
    "add_amount": { "uk": "...", "en": "...", "pl": "..." },
    ...
  }
  ```
  
- Use helper t(key, lang, **kwargs) everywhere:
  ```bash
  await message.answer(t("add_amount", lang))
  ```
- Users can change language via /lang; the choice is saved to DB and applied to the per-chat command menu
  
---

## 🗺 Roadmap

- Cloud deploy (Render/Fly/Heroku) with webhook.
- Categories & analytics (weekly/monthly summaries, charts).
- Export CSV.
- Postgres option & migrations.

---  

## License

This project is distributed under the terms of the [MIT License](LICENSE).














