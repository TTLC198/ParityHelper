from tg_api import tg_api
from classes import User
from config import TG_TOKEN


class bot:
    def __init__(self):
        self.__tg = tg_api(TG_TOKEN)

    async def listen(self):
        offset = 0
        while True:
            try:
                events = await self.__tg.get_updates_in_objects(offset=offset, timeout=60)
                for event in events.result:
                    offset = event.update_id + 1
                    if event.message is not None:
                        yield event
            except BaseException as e:
                print(f'listen: {e}')

    async def get_me(self) -> User:
        try:
            res_dict = await self.__tg.get_me()
            return User.Schema().load(res_dict)
        except BaseException as e:
            print(f'get_chat_members: {e}')

    async def get_chat_members(self, chat_id: int):
        res = None
        try:
            res = await self.__tg.get_chat_admins(chat_id=chat_id)
        except BaseException as e:
            print(f'get_chat_members: {e}')
        return res

    async def change_chat_title(self, chat_id: int, title: str) -> int:
        res = 1
        try:
            chat = await self.__tg.get_chat(chat_id=chat_id)
            if chat != [] and chat.title != title:
                await self.__tg.set_chat_title(chat_id=chat_id, title=title)
                print(f'changed chat title: chat_id={chat_id}, title={title}, res={res}')
        except BaseException as e:
            res = e.code
            print(f'change_chat_title: {e}')
        return res

    async def is_user_admin_in_chat(self, user_id: int, chat_id: int) -> bool:
        try:
            admins = await self.__tg.get_chat_admins(chat_id=chat_id)
            return any(x['user']['id'] == user_id for x in admins)
        except BaseException as e:
            print(f'is_user_admin_in_chat: {e}')
        return False

    async def send_message(self, chat_id: int, message: str) -> int:
        res = 1
        try:
            await self.__tg.send_message(
                chat_id=chat_id,
                message=message)
        except BaseException as e:
            res = e
            print(f'send_message: {e}')

        return res
