from functools import partial
from random import randint

import pygame as pg

from AIs.move_ais import standing_ai
from attack import ProjectileAttack, operate_attacks, attacks, show_attacks
from character import Character, Boss
from config import width, height, screen, width_scale, height_scale
from menu import show_all_texts, operate_all_buttons, show_all_buttons
from utilities import menu_falser, start_timer, get_time_passed, battle_ender, text_hp_update

clock = pg.time.Clock()


def run():
    global timer
    game = True
    color = (0, 0, 0)
    while game:
        screen.fill(color)
        menu = menu_falser()
        if not menu:
            squar.show_char(screen)
            epic_face.show_char(screen)
            show_attacks(attacks)
            battle_ender(squar, epic_face)
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
            operate_attacks(attacks, squar, epic_face)
            text_hp_update(squar, epic_face)
        for e in events:
            operate_all_buttons(e)
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    game = False
                if e.key == pg.K_SPACE:
                    if get_time_passed(timer) >= 3:
                        squar.attack(epic_face)
                        timer = start_timer()


squar = Character('Sources/squar.png', width / 2, height / 2, 3, 30, 5, "None")
epic_face = Boss("Sources/epic_face.png", 4, 100, 1080, 540, standing_ai)
timer = start_timer()
run()
