from config import screen, used_lang
from views import Text
from Sources.Translation.lang import texts

start_text = Text(texts["exit_text_" + used_lang], 10, 10, 30, (255, 255, 255), "Comic Sans MS")

def show_all_texts():
    start_text.draw(screen)
