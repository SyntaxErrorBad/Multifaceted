import os
from ai_voice import speak


def open_file_by_path(path):
    os.startfile(path)
    speak("Ваша папка відкрита")
