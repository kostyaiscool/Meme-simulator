from typing import TYPE_CHECKING

import config as cfg
from views import Text, Button, TranslateButton
from Sources.Translation.lang import texts

exit_text = Text(texts["exit_text_" + cfg.used_lang], 170, 10, 30, (255, 255, 255),
                 "Comic Sans MS", "DEMO")
warning_text = Text(texts["demo_warn_" + cfg.used_lang], 960, 1040, 30, (255, 255, 255), "Comic Sans MS", 1)
player_hp_text = Text("Типо хп игрока типо крутой", 960, 1020, 30, (255, 255, 255), "Comic Sans MS", 2)
boss_hp_text = Text("А что мне писать то? ", 960, 20, 30, (255, 255, 255), "Comic Sans MS", 2)
instructions_text = Text(texts["attack_instruction_" + cfg.used_lang], 960, 100, 30, (255, 255, 255), "Comic Sans MS",
                         2)


def show_all_texts():
    exit_text.draw(cfg.screen)
    warning_text.draw(cfg.screen)
    player_hp_text.draw(cfg.screen)
    boss_hp_text.draw(cfg.screen)
    instructions_text.draw(cfg.screen)

def update_texts():
    exit_text.update_text(exit_text.text)
    warning_text.update_text(exit_text.text)
    instructions_text.update_text(exit_text.text)


def play():
    cfg.stage = 2


def settings():
    cfg.stage = 3


def main():
    cfg.stage = 1

def lang():
    cfg.stage = 4


# to_select_button = Button(texts["meme_select_" + cfg.used_lang], troll, 0, 500, 100, 50, 1, (0, 0, 0), 24)
settings_button = Button(texts["settings_" + cfg.used_lang], settings, 1820, 25, 200, 50, 1, (0, 0, 0), 24)
tutorial_button = Button(texts["starter_play_" + cfg.used_lang], play, 1832, 1055, 175, 50, 1, (0, 0, 0), 24)
back_button = Button(texts["back_" + cfg.used_lang], main, 1870, 25, 100, 50, 3, (0, 0, 0), 24)
# change_lang_button = Button(texts["change_lang_" + cfg.used_lang], lang, 960, 25, 300, 50, 3, (0, 0, 0),24)
# back_button1 = Button(texts["back_" + cfg.used_lang], settings, 1820, 0, 100, 50, 4, (0, 0, 0), 24)
#
# ua_button = TranslateButton("Українська(Ukrainian)", lang, 660, 75, 300, 50, 4, (128, 128, 0), 24)
# ru_button = TranslateButton("Русский(Russian)", lang, 660, 0, 300, 50, 4, (128, 0, 0), 24)
# en_button = TranslateButton("English", lang, 660, 150, 300, 50, 4, (0, 0, 0), 24)


def show_all_buttons():
    # to_select_button.draw(cfg.screen)
    settings_button.draw(cfg.screen)
    tutorial_button.draw(cfg.screen)
    back_button.draw(cfg.screen)
    # change_lang_button.draw(cfg.screen)
    # back_button1.draw(cfg.screen)
    #
    # ua_button.draw(cfg.screen)
    # ru_button.draw(cfg.screen)
    # en_button.draw(cfg.screen)


def operate_all_buttons(event):
    # to_select_button.operate(event)
    settings_button.operate(event)
    tutorial_button.operate(event)
    back_button.operate(event)
    # change_lang_button.operate(event)
    # back_button1.operate(event)
    #
    # ua_button.operate(event, update_texts)
    # ru_button.operate(event, update_texts)
    # en_button.operate(event, update_texts)


