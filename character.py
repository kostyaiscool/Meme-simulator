import pygame as pg
from config import width, height


class Character:
    def __init__(self, image, x, y, scale, speed, max_HP, HP, max_dmg, ability):
        self.formula = width * (scale / 2000)
        self.skin = pg.image.load(image)
        self.skin = pg.transform.scale(self.skin, (self.formula, self.formula))
        self.rect = self.skin.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.ability = ability
        print(self.formula)

    def show_char(self, screen):
        screen.blit(self.skin, (self.rect.x, self.rect.y))

    def move(self, dir):
        if dir == 'up' and self.rect.y > 0:
            self.rect.y -= self.speed
        elif dir == 'down' and self.rect.y < height - 40:
            self.rect.y += self.speed
        if dir == 'left' and self.rect.x > 0:
            self.rect.x -= self.speed
        elif dir == 'right' and self.rect.x < width - 40:
            self.rect.x += self.speed