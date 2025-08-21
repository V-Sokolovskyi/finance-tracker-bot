import sqlite3
from datetime import datetime 
from config import DB_PATH, OWNER_TELEGRAM_ID

def _conn():
    c = sqlite3.connect(DB_PATH)
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY,
            lang TEXT
        );
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            ttype TEXT CHECK(ttype IN ('income','expense')) NOT NULL,
            category TEXT NOT NULL,
            note TEXT,
            ts TEXT NOT NULL
        );
    """)
    return c

def get_user_lang(tg_id: int)-> str | None:
    conn = _conn()
    row = conn.execute(
        "SELECT lang FROM users WHERE telegram_id=?",
        (tg_id,)
    ).fetchone()
    conn.close()
    return row[0] if row else None

def set_user_lang(tg_id: int, lang: str):
    conn = _conn()
    conn.execute(
    """
        INSERT INTO users(telegram_id, lang)
        VALUES(?, ?)
        ON CONFLICT(telegram_id) DO UPDATE SET lang=excluded.lang
    """,
    (tg_id, lang)
    )
    conn.commit()
    conn.close()
    
def add_tx(user_id: int, amount: float, ttype: str, category: str, note: str | None):
    conn = _conn()
    ts = datetime.now().isoformat(" ", "seconds")
    conn.execute(
        "INSERT INTO transactions(user_id,amount,ttype,category,note,ts) VALUES(?,?,?,?,?,?)",
        (user_id, amount, ttype, category, note, ts)
    )
    conn.commit()
    conn.close()
    return ts

def list_tx(user_id: int, all_for_owner: bool = False, limit: int = 20):
    conn = _conn()
    if all_for_owner and OWNER_TELEGRAM_ID and user_id == OWNER_TELEGRAM_ID:
        rows = conn.execute(
            "SELECT user_id, amount, ttype, category, note, ts FROM transactions ORDER BY ts DESC LIMIT ?",
            (limit,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT user_id, amount, ttype, category, note, ts FROM transactions WHERE user_id=? ORDER BY ts DESC LIMIT ?",
            (user_id, limit)
        ).fetchall()
    conn.close()
    return rows