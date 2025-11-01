import pygame as pg

from config import width_scale, height_scale, screen


class ProjectileAttack():
    def __init__(self, damage, x, y, scale, direction, image, speed):
        self.damage = damage
        self.image = image
        self.x = x
        self.y = y
        self.scale = scale
        self.dir = direction
        self.skin = pg.image.load(image)
        self.skin = pg.transform.scale(self.skin, (self.scale * width_scale, self.scale * width_scale))
        self.rect = self.skin.get_rect()
        self.rect.x = x * width_scale
        self.rect.y = y * height_scale
        self.speed = speed * width_scale

    def show_attack(self, screen):
        if self.rect != None:
            screen.blit(self.skin, (self.rect.x, self.rect.y))

    def operate_attack(self, player, boss):
        if self.rect != None:
            if self.dir == "left":
                self.rect.x -= self.speed
            elif self.dir == "up":
                self.rect.y -= self.speed
            elif self.dir == "right":
                self.rect.x += self.speed
            elif self.dir == "down":
                self.rect.y += self.speed

            if self.rect.colliderect(player.rect):
                player.hp -= self.damage
                print(player.hp)
                self.rect = None
            elif self.rect.colliderect(boss.rect):
                boss.hp -= self.damage
                print(boss.hp)
                self.rect = None


test_attack = ProjectileAttack(29, 1900, 540, 50, "left", "Sources/squar.png", 10)
attacks = [test_attack]


def show_attacks(list):
    for i in list:
        i.show_attack(screen)


def operate_attacks(list, char, boss):
    for i in list:
        i.operate_attack(char, boss)


def spawn_projectile():
    from random import randint
    y = randint(-1000, 1000)
    attacks.append(ProjectileAttack(29, 1900, y, 50, "left", "Sources/squar.png", 10))
