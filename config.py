import pygame
import win32api
import win32con
import ctypes
import locale
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
lang_code = locale.windows_locale.get(lang_id)
used_lang = lang_code.split("_")
print(used_lang[0])
pygame.display.set_caption("Мемный симулятор")
pygame.display.set_icon(screen)
# cube_width  = (25 / 480) * screen_width
# cube_height = (25 / 360) * screen_height