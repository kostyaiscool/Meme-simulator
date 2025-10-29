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
        self.font = pg.font.SysFont(self.font_name, int(self.size * cfg.width_scale))
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(topleft=(int(self.x * cfg.width_scale), int(self.y * cfg.height_scale)))
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
        self.skin = pg.Surface((int(sx * cfg.width_scale), int(sy * cfg.height_scale)))
        self.skin.fill(color)
        # self.rect = self.skin.get_rect()
        self.rect = self.skin.get_rect(topleft=(int(self.x * cfg.width_scale), int(self.y * cfg.height_scale)))
        self.rect.x = int(self.x * cfg.width_scale)
        self.rect.y = int(self.y * cfg.height_scale)
        self.sx = sx
        self.sy = sy
        self.text_size = text_size

    def draw(self, surface):
        if cfg.stage == self.menu_stage:
            surface.blit(self.skin, self.rect)
            pg.draw.rect(surface, (255, 255, 255), self.rect, int(3 * cfg.width_scale))
            text = Text(self.text, self.x + 10, self.y + 5, self.text_size, (255, 255, 255), "Comic Sans MS",
                        self.menu_stage)
            text.draw(surface)

    def operate(self, events):
        if events.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.method()
