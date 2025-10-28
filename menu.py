import config
import config as cfg
from views import Text, Button
from Sources.Translation.lang import texts

exit_text = Text(texts["exit_text_" + cfg.used_lang], 10, 10, 30, (255, 255, 255),
                 "Comic Sans MS", "DEMO")


def show_all_texts():
    exit_text.draw(cfg.screen)


def set_stage():
    cfg.stage = 4
    print(cfg.stage)


test_button = Button("Test", set_stage, 1000, 500, 100, 50, 1, (0, 0, 0), 35)


def show_all_buttons():
    test_button.draw(cfg.screen)


def operate_all_buttons(event):
    test_button.operate(event)
