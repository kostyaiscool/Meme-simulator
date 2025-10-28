from typing import TYPE_CHECKING
import pygame as pg
import config as cfg

pg.init()


class Text:
    def __init__(self, text, x, y, size, color, font_name, stage):
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.font_name = font_name
        self.font = pg.font.SysFont(self.font_name, int(cfg.width * (self.size / 1920)))
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(topleft=(int(cfg.width * (self.x / 1920)), int(cfg.height * (self.y / 1080))))
        self.stage = stage

    def update_text(self, new_text):
        self.text = new_text
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        if self.stage == cfg.stage and self.stage != "DEMO":
            surface.blit(self.rendered, self.rect)
        elif self.stage == "DEMO":
            surface.blit(self.rendered, self.rect)


class Button:
    def __init__(self, text, method, x, y, sx, sy, menu_stage, color, text_size):
        self.menu_stage = menu_stage
        self.text = text
        self.method = method
        self.x = x
        self.y = y
        self.skin = pg.Surface((int(cfg.width * (sx / 1920)), int(cfg.height * (sy / 1080))))
        self.skin.fill(color)
        self.rect = self.skin.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sx = sx
        self.sy = sy
        self.text_size = text_size

    def draw(self, surface):
        if cfg.stage == self.menu_stage:
            surface.blit(self.skin, (self.rect.x, self.rect.y))
            pg.draw.rect(surface, (255, 255, 255), self.rect, 3)
            text = Text(self.text, self.x + 10, self.y, self.text_size, (255, 255, 255), "Comic Sans MS", self.menu_stage)
            text.draw(surface)

    def operate(self, events):
        if events.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.x <= mouse_x <= self.rect.x + self.sx and self.rect.y <= mouse_y <= self.rect.y + self.sy:
                self.method()
