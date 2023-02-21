import asyncio
import threading

import logic

from bot import bot
from listener_util import start as listener_start
from scheduler_util import start as scheduler_start
from config import BOT_RESTORE, MAX_CHATS
from messages import SETTING, BOT_NEWS


def create_task(task):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(task)
    loop.run_forever()


if __name__ == '__main__':
    tgBot = bot()

    active_chats = 0
    if BOT_RESTORE == 1:
        for i in range(1, MAX_CHATS + 1):
            if tgBot.send_message(i, BOT_NEWS + '\n\n' + SETTING + logic.curr_week_msg()) == 1:
                active_chats += 1
    print(f'{active_chats} chats are active')

    try:
        threads = [
            threading.Thread(target=create_task, args=(listener_start(tgBot),)),
            threading.Thread(target=create_task, args=(scheduler_start(tgBot),)),
        ]
        [t.start() for t in threads]
        [t.join() for t in threads]
    except KeyboardInterrupt:
        pass
