from random import randint

from attack import spawn_projectile
from config import width_scale, width, height, height_scale
from utilities import get_time_passed, start_timer

timer = start_timer()
hdir = 1
vdir = 1


def mild_ai(char, speed):
    global hdir, vdir, timer
    if get_time_passed(timer) >= 3:
        hdir = randint(1, 3)
        vdir = randint(1, 3)
        spawn_projectile()
        timer = start_timer()

    if char.rect.x <= 0:
        hdir = randint(2, 3)
    elif char.rect.x >= width - 60 * width_scale:
        hdir = 1
    if char.rect.y <= 0:
        vdir = randint(2, 3)
    elif char.rect.y >= height - 60 * height_scale:
        vdir = 1

    if hdir == 1 and char.rect.x > 0:
        char.rect.x -= speed
    elif hdir == 2 and char.rect.x < width - 60 * width_scale:
        char.rect.x += speed
    if vdir == 1 and char.rect.y > 0:
        char.rect.y -= speed
    elif vdir == 2 and char.rect.y < height - 60 * height_scale:
        char.rect.y += speed

def standing_ai(char, speed):
    global timer
    if get_time_passed(timer) >= 0.05:
        spawn_projectile()
        timer = start_timer()