import os


TOKEN = os.getenv('TOKEN')
KEY = os.getenv('KEY')
SERVER = os.getenv('SERVER')
TS = int(os.getenv('TS'))
SHIFT_PARITY = int(os.getenv('SHIFT_PARITY'))
TIME_ZONE_OFFSET = int(os.getenv('TIME_ZONE_OFFSET'))
GROUP_ID = 202243542
DB_URL = os.getenv('DATABASE_URL')
BOT_RESTORE = int(os.getenv('BOT_RESTORE'))
MAX_CHATS = int(os.getenv('MAX_CHATS'))
