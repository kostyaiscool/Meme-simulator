import config as cfg
import time


def menu_falser():
    if cfg.stage == 2:
        return False
    else:
        return True


def start_timer():
    return time.time()


def get_time_passed(start_time):
    return time.time() - start_time


# a = start_timer()
# time.sleep(5)
# print(get_time_passed(a))
