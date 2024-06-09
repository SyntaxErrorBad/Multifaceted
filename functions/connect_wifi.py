import subprocess
from logs import logger
from ai_voice import speak


def connect_to_wifi(ssid):
    command = f'netsh wlan connect name="{ssid}"'

    try:
        output = subprocess.check_output(command, shell = True, stderr = subprocess.STDOUT, text = True)
        speak("Я успішно вас підключив")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка подключения: {e.output}")
        speak("Нажаль виникла помилка підчас підключення")
