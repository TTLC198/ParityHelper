import os

# TG bot settings
TG_TOKEN = os.getenv('TG_TOKEN')

SHIFT_PARITY = int(os.getenv('SHIFT_PARITY'))
TIME_ZONE_OFFSET = int(os.getenv('TIME_ZONE_OFFSET'))

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

BOT_RESTORE = int(os.getenv('BOT_RESTORE'))
MAX_CHATS = int(os.getenv('MAX_CHATS'))
