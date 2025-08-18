import pygame as pg
from character import Character
from config import width, height, screen
from views import show_all_texts
clock = pg.time.Clock()


def run():
    game = True
    color = (0, 0, 0)

    while game:
        screen.fill(color)
        squar.show_char(screen)
        show_all_texts()
        pg.display.flip()
        clock.tick(60)
        events = pg.event.get()
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            squar.move('up')
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            squar.move('down')
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            squar.move('left')
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            squar.move('right')
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    game = False


squar = Character('Sources/squar.png', width / 2, height / 2, 20, 3, 30, 30, 5, "None")
run()
