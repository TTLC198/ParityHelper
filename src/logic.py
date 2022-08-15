import datetime as dt

from config import SHIFT_PARITY, TIME_ZONE_OFFSET
from messages import EVEN_WEEK, ODD_WEEK


def get_curr_week_parity() -> bool:
    now = dt.datetime.now() + dt.timedelta(hours=TIME_ZONE_OFFSET)
    parity = (int(now.strftime('%W')) + SHIFT_PARITY) % 2 == 1
    return parity

def curr_week_msg() -> str:
    return ODD_WEEK if get_curr_week_parity() else EVEN_WEEK
