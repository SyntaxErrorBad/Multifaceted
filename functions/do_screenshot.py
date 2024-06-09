import pyautogui
import os
from ai_voice import speak

import win32clipboard
from dotenv import load_dotenv
from datetime import datetime
import io
from PIL import Image


load_dotenv("data/.env")


def screenshot():
    take_screenshot = pyautogui.screenshot()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_path = f"../data/screenshots/screenshot_{current_time}.png"
    take_screenshot.save(filename_path)
    screenshot_access = os.getenv('SAVE_SCREENSHOT').split(',')
    if screenshot_access[0] == 'True':
        save_in_buffer(filename_path)
    if screenshot_access[-1] == 'False':
        os.remove(filename_path)
    speak("Скріншот зроблено")


def save_in_buffer(filename_path):
    image = Image.open(filename_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    send_to_clipboard(win32clipboard.CF_DIB, data)


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
