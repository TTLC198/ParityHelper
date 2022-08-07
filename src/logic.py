import datetime as dt

from config import SHIFT_PARITY, TIME_ZONE_OFFSET


def get_curr_week_parity() -> bool:
    now = dt.datetime.now() + dt.timedelta(hours=TIME_ZONE_OFFSET)
    parity = (int(now.strftime('%W')) + SHIFT_PARITY) % 2 == 1
    return parity
