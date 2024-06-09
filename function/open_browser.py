import webbrowser
from ai_voice import speak


def open_url_browser(url):
    webbrowser.open(url)
    speak("Браузер відкритий")
