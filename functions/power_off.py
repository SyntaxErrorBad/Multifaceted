import os
import platform
from logs import logger
from ai_voice import speak


def shutdown_computer():
    system = platform.system()
    logger.info("PC ShutDown")
    speak("До нових зустрічей")
    if system == 'Windows':
        os.system('shutdown /s /t 1')
    elif system == 'Linux':
        os.system('shutdown now')
    elif system == 'Darwin':
        os.system('sudo shutdown -h now')
    else:
        logger.error(f'Unsupported operating system: {system}')

