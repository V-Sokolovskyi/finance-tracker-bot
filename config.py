from dotenv import load_dotenv
import os 

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_TELEGRAM_ID = int(os.getenv("OWNER_TELEGRAM_ID", "0"))
DB_PATH = os.getenv("DB_PATH", "finance.db")