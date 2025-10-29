import config as cfg
from views import Text, Button
from Sources.Translation.lang import texts

exit_text = Text(texts["exit_text_" + cfg.used_lang], 10, 10, 30, (255, 255, 255),
                 "Comic Sans MS", "DEMO")
warning_text = Text(texts["demo_warn_" + cfg.used_lang], 650, 1020, 30, (255, 255, 255), "Comic Sans MS", 1)


def show_all_texts():
    exit_text.draw(cfg.screen)
    warning_text.draw(cfg.screen)


def troll():
    print("Стену 1000 словами не пробъешь, но пробъешь кулаком. Не думай об этом просто иди в шахту")


to_select_button = Button(texts["meme_select_" + cfg.used_lang], troll, 0, 500, 100, 50, 1, (0, 0, 0), 24)
settings_button = Button(texts["meme_select_" + cfg.used_lang], troll, 1820, 0, 100, 50, 1, (0, 0, 0), 24)


def show_all_buttons():
    to_select_button.draw(cfg.screen)
    settings_button.draw(cfg.screen)


def operate_all_buttons(event):
    to_select_button.operate(event)
