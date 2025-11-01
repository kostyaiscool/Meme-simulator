import config as cfg
import time

from attack import attacks
from menu import player_hp_text, boss_hp_text


def menu_falser():
    if cfg.stage == 2:
        return False
    else:
        return True


def start_timer():
    return time.time()


def get_time_passed(start_time):
    return time.time() - start_time

def battle_ender(player, boss):
    if player.hp <= 0 or boss.hp <= 0:
        cfg.stage = 1
        player.hp = player.max_hp
        boss.hp = boss.max_hp
        attacks.clear()
        player.rect.x = player.x
        player.rect.y = player.y
        boss.rect.x = boss.x
        boss.rect.y = boss.y

def text_hp_update(player, boss):
    player_hp_text.update_text(str(player.hp))
    boss_hp_text.update_text(str(boss.hp))
# a = start_timer()
# time.sleep(5)
# print(get_time_passed(a))
