import psycopg2

from config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT


class Repository:
    def __init__(self):
        self.__connection = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
        cursor = self.__connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS chat (chat_id bigint not null constraint chat_pk primary key, even_week_name TEXT, odd_week_name TEXT)")
        cursor.close()

        self.__connection.commit()

    def get_chat(self, chat_id: int):
        cursor = self.__connection.cursor()

        cursor.execute("SELECT * FROM chat WHERE chat_id = %s;", (chat_id,))
        res = cursor.fetchone()
        cursor.close()

        return res

    def get_chats_odd_week_names(self):
        cursor = self.__connection.cursor()

        cursor.execute("SELECT chat_id, odd_week_name FROM chat;")
        res = cursor.fetchall()
        cursor.close()

        return res

    def get_chats_even_week_names(self):
        cursor = self.__connection.cursor()

        cursor.execute("SELECT chat_id, even_week_name FROM chat;")
        res = cursor.fetchall()
        cursor.close()

        return res

    def add_chat(self, chat_id: int, even_week_name: str, odd_week_name: str):
        cursor = self.__connection.cursor()

        cursor.execute("INSERT INTO chat VALUES (%s, %s, %s);", (chat_id, even_week_name, odd_week_name))
        cursor.close()

        self.__connection.commit()

    def change_chat(self, chat_id: int, even_week_name: str, odd_week_name: str):
        if self.get_chat(chat_id):
            cursor = self.__connection.cursor()
            cursor.execute("UPDATE chat SET even_week_name = %s, odd_week_name = %s WHERE chat_id = %s;",
                (even_week_name, odd_week_name, chat_id))
            cursor.close()

            self.__connection.commit()
        else:
            self.add_chat(chat_id, even_week_name, odd_week_name)
