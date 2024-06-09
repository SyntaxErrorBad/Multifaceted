import pyttsx3


def speak(text):
    """""Ініціалізація pyttsx3 і відтворення тексту вголос"""""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
