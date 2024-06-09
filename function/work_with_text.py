import pyperclip
import keyboard
import time
import os
from dotenv import load_dotenv
from googletrans import Translator
from ai_voice import speak
from logs import logger

load_dotenv("data/.env")


def control_text(action):
    if action == "переклади":
        translate_selected_text()
    else:
        copy_selected_text()


def copy_selected_text():
    try:
        keyboard.press_and_release('ctrl+c')
        speak("Я скопіював")
    except Exception as e:
        logger.error(e)


def translate_selected_text():
    copy_selected_text()
    time.sleep(0.1)
    copied_text = pyperclip.paste()
    translator = Translator()
    translated = translator.translate(copied_text, dest = os.getenv('TRANSLATED_TEXT').lower())
    speak(f"Там написано: {translated}")
