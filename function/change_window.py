import pygetwindow as gw
import psutil
import win32process
from ai_voice import speak


def get_window_process_name(hwnd):
    """Отримання імені процеса"""
    try:
        thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(process_id)
        return process.name()
    except psutil.NoSuchProcess:
        return None


def change_current_window(window_exe):
    all_windows = gw.getAllWindows()
    for window in all_windows:
        process_name = get_window_process_name(window._hWnd)
        if process_name == window_exe:
            windows = gw.getWindowsWithTitle(window.title)
            windows[0].restore()
            windows[0].activate()
    speak("Ваше вікно відкрите")
