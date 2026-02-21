import time
from random import randint
from attack import spawn_projectile
from utilities import get_time_passed, start_timer
# from views import Dialogue

# timer = start_timer()
# dialogue = True
start_time = time.time()
def ef_sequence(boss):
    global start_time
    # global timer, dialogue
    if 100 >= boss.hp > 50:
        # if dialogue:
        #     if get_time_passed(timer) > 2:
        #         while dialogue:
        #             pass
                    # d1 = Dialogue(["test", "test"], (255, 255, 255), 24, 2, timer)
                # dialogue = False
        # else:
        # while True:
        if time.time() - start_time > 0.1:
            spawn_projectile(3, 1890, randint(-1000, 1000), 25, "left", "Sources/squar.png", 10, False)
            start_time = time.time()
