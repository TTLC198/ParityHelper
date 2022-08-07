import threading

from bot import Bot
from listener_util import start as listener_start
from scheduler_util import start as scheduler_start


if __name__ == '__main__':
    bot = Bot()

    t1 = threading.Thread(target=listener_start, args=(bot,))
    t2 = threading.Thread(target=scheduler_start, args=(bot,))
    t1.start()
    t2.start()
