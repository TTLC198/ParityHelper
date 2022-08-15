import threading

import logic

from bot import Bot
from listener_util import start as listener_start
from scheduler_util import start as scheduler_start
from config import BOT_RESTORE, MAX_CHATS
from messages import SETTING, BOT_NEWS


if __name__ == '__main__':
    bot = Bot()

    acvive_chats = 0
    if BOT_RESTORE == 1:
        for i in range(1, MAX_CHATS + 1):
            if bot.send_message(i, BOT_NEWS + '\n\n' + SETTING + logic.curr_week_msg()) == 1:
                acvive_chats += 1
    print(f'{acvive_chats} chats are active')

    t1 = threading.Thread(target=listener_start, args=(bot,))
    t2 = threading.Thread(target=scheduler_start, args=(bot,))
    t1.start()
    t2.start()
