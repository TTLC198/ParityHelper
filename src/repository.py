import sqlite3

from config import DB_NAME


class Repository:
    def __init__(self):
        self.__connection = sqlite3.connect(DB_NAME)
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS chat (chat_id INTEGER, even_week_name TEXT, odd_week_name TEXT)")
        self.__connection.commit()

    def get_chat(self, chat_id: int):
        res = self.__cursor.execute("SELECT * FROM chat WHERE chat_id = ?", (chat_id,)).fetchall()
        return res[0] if res else None

    def get_chats_odd_week_names(self):
        res = self.__cursor.execute("SELECT chat_id, odd_week_name FROM chat").fetchall()
        return res

    def get_chats_even_week_names(self):
        res = self.__cursor.execute("SELECT chat_id, even_week_name FROM chat").fetchall()
        return res

    def add_chat(self, chat_id: int, even_week_name: str, odd_week_name: str):
        self.__cursor.execute("INSERT INTO chat VALUES (?, ?, ?)", (chat_id, even_week_name, odd_week_name))
        self.__connection.commit()

    def change_chat(self, chat_id: int, even_week_name: str, odd_week_name: str):
        if self.get_chat(chat_id):
            self.__cursor.execute("UPDATE chat SET even_week_name = ?, odd_week_name = ? WHERE chat_id = ?",
                (even_week_name, odd_week_name, chat_id))
        else:
            self.add_chat(chat_id, even_week_name, odd_week_name)
        self.__connection.commit()
