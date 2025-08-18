import pygame as pg
from config import screen

pg.init()
class Text:
    def __init__(self, text, x, y, size, color, font_name):
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.font_name = font_name
        self.font = pg.font.SysFont(self.font_name, self.size)
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(topleft=(self.x, self.y))  # <-- Установка позиции

    def update_text(self, new_text):
        self.text = new_text
        self.rendered = self.font.render(self.text, True, self.color)
        self.rect = self.rendered.get_rect(topleft=(self.x, self.y))  # <-- Не забыть обновить позицию

    def draw(self, surface):
        surface.blit(self.rendered, self.rect)

# экземпляр
start_text = Text("Нажми Esc для выхода", 10, 10, 30, (255, 255, 255), "Comic Sans MS")

def show_all_texts():
    start_text.draw(screen)
