import pygame as pg
import config as cfg
# from utilities import get_time_passed

pg.init()


class Text:
    def __init__(self, text, x, y, size, color, font_name, stage):
        self.text = text
        # self.x = int(x * cfg.width_scale - size / 2)
        self.x = int(x * cfg.width_scale)
        self.y = int(y * cfg.height_scale)
        self.size = int(size * cfg.width_scale)
        self.color = color
        self.font_name = font_name
        self.font = pg.font.SysFont(self.font_name, self.size)
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(center=(self.x, self.y))
        # self.rect = self.rendered.get_rect(center=(0, 0))
        # self.rect.x = self.x
        # self.rect.y = self.y
        # self.rect = self.rendered.get_rect()
        self.stage = stage

    def update_text(self, new_text):
        self.text = new_text
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        if self.stage == cfg.stage and self.stage != "DEMO":
            # self.text.rect.center = self.rect.center
            surface.blit(self.rendered, self.rect)
        elif self.stage == "DEMO":
            surface.blit(self.rendered, self.rect)


class Button:
    def __init__(self, text, method, x, y, sx, sy, menu_stage, color, text_size):
        self.menu_stage = menu_stage
        self.text = text
        self.method = method
        # self.x = int(x * cfg.width_scale - sx / 2)
        # self.y = int(y * cfg.height_scale - sy / 2)
        self.x = int(x * cfg.width_scale)
        self.y = int(y * cfg.height_scale)
        self.skin = pg.Surface((sx, sy))
        self.skin.fill(color)
        self.rect = self.skin.get_rect(center=(self.x, self.y))
        # self.rect = self.skin.get_rect(center=(0, 0))
        # self.rect.x = self.x
        # self.rect.y = self.y
        self.sx = sx
        self.sy = sy
        self.text_size = text_size
        self.text = Text(self.text, self.rect.centerx / cfg.width_scale, self.rect.centery / cfg.height_scale, self.text_size, (255, 255, 255), "Comic Sans MS",
                        self.menu_stage)

    def draw(self, surface):
        if cfg.stage == self.menu_stage:
            surface.blit(self.skin, self.rect)
            pg.draw.rect(surface, (255, 255, 255), self.rect, int(3 * cfg.width_scale))
            self.text.draw(surface)

    def operate(self, events):
        if cfg.stage == self.menu_stage:
            if events.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.method()


class TranslateButton:
    def __init__(self, text, lang, x, y, sx, sy, menu_stage, color, text_size):
        self.menu_stage = menu_stage
        self.text = text
        self.lang = lang
        self.x = x
        self.y = y
        self.skin = pg.Surface((int(sx * cfg.width_scale), int(sy * cfg.height_scale)))
        self.skin.fill(color)
        # self.rect = self.skin.get_rect()
        self.rect = self.skin.get_rect(center=(int(self.x * cfg.width_scale), int(self.y * cfg.height_scale)))
        self.rect.x = int(self.x * cfg.width_scale)
        self.rect.y = int(self.y * cfg.height_scale)
        self.sx = sx
        self.sy = sy
        self.text_size = text_size

    def draw(self, surface):
        if cfg.stage == self.menu_stage:
            surface.blit(self.skin, self.rect)
            pg.draw.rect(surface, (255, 255, 255), self.rect, int(3 * cfg.width_scale))
            text = Text(self.text, self.x, self.y, self.text_size, (255, 255, 255), "Comic Sans MS",
                        self.menu_stage)
            text.draw(surface)

    def operate(self, events, update):
        if cfg.stage == self.menu_stage:
            if events.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    cfg.used_lang = self.lang
                    print(cfg.used_lang)
                    update()