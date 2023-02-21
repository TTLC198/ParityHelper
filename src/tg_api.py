from typing import Optional

import aiohttp

from classes import GetUpdatesResponse, SendMessageResponse, Chat


class tg_api:
    def __init__(self, token: str = ''):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    async def get_me(self) -> dict:
        url = self.get_url("getMe")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return (await resp.json())['result']

    async def get_updates(self, offset: Optional[int] = None, timeout: int = 0) -> dict:
        url = self.get_url("getUpdates")
        params = {}
        if offset:
            params['offset'] = offset
        if timeout:
            params['timeout'] = timeout
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                return await resp.json()

    async def get_updates_in_objects(self, offset: Optional[int] = None, timeout: int = 0) -> GetUpdatesResponse:
        res_dict = await self.get_updates(offset=offset, timeout=timeout)
        return GetUpdatesResponse.Schema().load(res_dict)

    async def send_message(self, chat_id: int, message: str) -> SendMessageResponse:
        url = self.get_url("sendMessage")
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                res_dict = await resp.json()
                return SendMessageResponse.Schema().load(res_dict)

    async def set_chat_title(self, chat_id: int, title: str) -> dict:
        url = self.get_url("setChatTitle")
        payload = {
            'chat_id': chat_id,
            'title': title
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                return (await resp.json())['result']

    async def get_chat(self, chat_id: int) -> Chat:
        url = self.get_url("getChat")
        payload = {
            'chat_id': chat_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                res_dict = await resp.json()
                if 'result' in res_dict:
                    return Chat.Schema().load(res_dict['result'])

    async def get_chat_admins(self, chat_id: int) -> dict:
        url = self.get_url("getChatAdministrators")
        payload = {
            'chat_id': chat_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                res_dict = await resp.json()
                if 'result' in res_dict:
                    return res_dict['result']
