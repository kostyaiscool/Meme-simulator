import ctypes
import locale
import pygame as pg
pg.init()
info = pg.display.Info()
width = info.current_w
height = info.current_h
print("Ширина:", width, "Высота:", height)
screen = pg.display.set_mode((width, height), pg.RESIZABLE)
lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
lang_code = locale.windows_locale.get(lang_id)
used_lang = lang_code.split("_")[0]
print(used_lang)
pg.display.set_caption("Мемный симулятор")
pg.display.set_icon(screen)
# cube_width  = (25 / 480) * screen_width
# cube_height = (25 / 360) * screen_height