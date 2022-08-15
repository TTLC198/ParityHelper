import datetime as dt

import logic

from time import sleep

from messages import BOT_IS_NOT_ADMIN
from config import TIME_ZONE_OFFSET
from bot import Bot
from repository import Repository


def start(bot: Bot):
    while True:
        repository = Repository()
        if logic.get_curr_week_parity():
            chats = repository.get_chats_odd_week_names()
        else:
            chats = repository.get_chats_even_week_names()

        print(f'{len(chats)} chats to check')

        for chat in chats:
            res = bot.change_chat_title(chat[0], chat[1])
            if res == 925:
                bot.send_message(chat[0], BOT_IS_NOT_ADMIN)

        now = dt.datetime.now() + dt.timedelta(hours=TIME_ZONE_OFFSET)
        next = now + dt.timedelta(days=7-now.weekday())
        next_monday = dt.datetime(next.year, next.month, next.day) + dt.timedelta(hours=TIME_ZONE_OFFSET)
        print(f'time now: {now}, next monday: {next_monday}, odd week: {logic.get_curr_week_parity()}')

        sleep((next_monday - now).total_seconds() + 1)
