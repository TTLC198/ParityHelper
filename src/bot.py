import vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.exceptions import ApiError

from config import TOKEN, TS, KEY, SERVER, GROUP_ID


class Bot:
    def __init__(self):
        self.__vk_session = vk_api.VkApi(token=TOKEN)
        self.__vk = self.__vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.__vk_session, GROUP_ID)

    def listen(self):
        while True:
            try:
                for event in self.longpoll.listen():
                    yield event
            except ApiError as e:
                print(f'listen: {e.error}, {e.code}')

    def get_chat_members(self, chat_id: int):
        res = None
        try:
            res = self.__vk.messages.getConversationMembers(peer_id=2000000000+chat_id)
        except ApiError as e:
            print(f'get_chat_members: {e.error}, {e.code}, chat_id: {chat_id}')
        return res

    def change_chat_title(self, chat_id: int, title: str) -> int:
        res = 1
        try:
            chat = self.__vk.messages.getConversationsById(peer_ids=2000000000+chat_id)['items']
            if chat != [] and chat[0]['chat_settings']['title'] != title:
                self.__vk.messages.editChat(chat_id=chat_id, title=title)
        except ApiError as e:
            res = e.code
            print(f'change_chat_title: {e.error}, {e.code}, chat_id: {chat_id}')
        return res

    def is_user_admin_in_chat(self, user_id: int, chat_id: int) -> bool:
        res = False
        try:
            response = self.__vk.messages.getConversationMembers(peer_id=2000000000+chat_id)
            for member in response['items']:
                if member['member_id'] == user_id and member['is_admin']:
                    res = True
        except ApiError as e:
            print(f'is_user_admin_in_chat: {e.error}, {e.code}, user_id: {user_id}, chat_id: {chat_id}')
        return res

    def send_message(self, chat_id: int, message: str):
        try:
            self.__vk.messages.send(
                chat_id=chat_id,
                message=message,
                key=KEY,
                ts=TS,
                server=SERVER,
                random_id=vk_api.utils.get_random_id())
        except ApiError as e:
            print(f'send_message: {e.error}, {e.code}, chat_id: {chat_id}')
