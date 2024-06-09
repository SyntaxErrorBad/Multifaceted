import os
from ai_voice import speak


def start_application(app_path):
    os.startfile(app_path)
    speak("Ваш додаток відкритий")