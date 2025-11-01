from functools import partial
from random import randint

import pygame as pg

from AIs.move_ais import test_ai
from character import Character, Boss
from config import width, height, screen, width_scale, height_scale
from menu import show_all_texts, operate_all_buttons, show_all_buttons
from utilities import menu_falser, start_timer, get_time_passed

clock = pg.time.Clock()


def run():
    game = True
    color = (0, 0, 0)
    while game:
        screen.fill(color)
        menu = menu_falser()
        if not menu:
            squar.show_char(screen)
            epic_face.show_char(screen)
        show_all_texts()
        show_all_buttons()
        pg.display.flip()
        clock.tick(60)
        events = pg.event.get()
        keys = pg.key.get_pressed()
        if not menu:
            if keys[pg.K_UP] or keys[pg.K_w]:
                squar.move('up')
            elif keys[pg.K_DOWN] or keys[pg.K_s]:
                squar.move('down')
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                squar.move('left')
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                squar.move('right')
            epic_face.operate_ai()
        for e in events:
            operate_all_buttons(e)
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    game = False


squar = Character('Sources/squar.png', width / 2, height / 2, 3, 30, 5, "None")
epic_face = Boss("Sources/epic_face.png", 4, 3298328923, 1080, 540, test_ai)
run()
