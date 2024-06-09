import pygetwindow as gw
import win32con
import win32gui
from ai_voice import speak


def control_window(task):
    active_window = gw.getActiveWindow()
    if task == "закрить":
        active_window.close()
        speak("Закрив")
    elif task == "заховать":
        hwnd = active_window._hWnd
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        speak("Заховав")
    else:
        speak("Щось не так, спробуйте знову")
