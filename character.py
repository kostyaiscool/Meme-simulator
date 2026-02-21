from random import randint

import pygame as pg
from config import width, height, width_scale, height_scale


class Character:
    def __init__(self, image, x, y, speed, max_hp, max_dmg, ability):
        self.formula = int(30 * width_scale)
        self.skin = pg.image.load(image)
        self.skin = pg.transform.scale(self.skin, (self.formula, self.formula))
        self.rect = self.skin.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.speed = speed * width_scale
        self.ability = ability
        self.hp = max_hp
        self.max_hp = max_hp
        self.damage = max_dmg

    def show_char(self, screen):
        screen.blit(self.skin, (self.rect.x, self.rect.y))

    def move(self, dir):
        if dir == 'up' and self.rect.y > 0:
            self.rect.y -= self.speed
        elif dir == 'down' and self.rect.y < height - 30 * height_scale:
            self.rect.y += self.speed
        if dir == 'left' and self.rect.x > 0:
            self.rect.x -= self.speed
        elif dir == 'right' and self.rect.x < width - 30 * width_scale:
            self.rect.x += self.speed

    def attack(self, boss):
        if self.rect.colliderect(boss.rect):
            boss.hp -= self.damage


class Boss:
    def __init__(self, image, speed, max_hp, x, y, ai):
        self.formula = int(60 * width_scale)
        self.skin = pg.image.load(image)
        self.skin = pg.transform.scale(self.skin, (self.formula, self.formula))
        self.rect = self.skin.get_rect()
        self.rect.x = x * width_scale
        self.rect.y = y * height_scale
        self.speed = speed * width_scale
        self.ai = ai
        self.hp = max_hp
        self.max_hp = max_hp
        self.x = x
        self.y = y
        # self.surface = surface
        # self.events = events

    def operate_ai(self):
        self.ai(char=self, speed=self.speed)

    def show_char(self, screen):
        screen.blit(self.skin, (self.rect.x, self.rect.y))
