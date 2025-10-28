import ctypes
import locale
import pygame as pg

from Translation.lang_debug import available_langs

pg.init()
info = pg.display.Info()
width = info.current_w
height = info.current_h
print("Ширина: " + str(width) + " Высота: " + str(height))
screen = pg.display.set_mode((width, height))

lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
lang_code = locale.windows_locale.get(lang_id)
used_lang = lang_code.split("_")[0]
print("Язык: " + used_lang)

if used_lang not in available_langs:
    used_lang = "en"
    print("Языка нету:(")

pg.display.set_caption("Мемный симулятор")
icon = pg.image.load("Sources/game_iconVPA0.1.png")
pg.display.set_icon(icon)
# cube_width  = (25 / 480) * screen_width
# cube_height = (25 / 360) * screen_height

stage = 1
