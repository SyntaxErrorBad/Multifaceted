import speech_recognition as sr
import asyncio
from ai_base import base
from logs import logger
from ai_voice import speak


async def recognize_speech_from_mic(recognizer, microphone):
    """Асинхронне розпізнавання мови з мікрофону"""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration = 0.5)
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio, language = "uk-UA")
        await process_text(response)
    except sr.UnknownValueError:
        logger.error("Audio could not be recognised")
        speak("Я не зміг розпізнати, повторіть будь ласка")
    except sr.RequestError as e:
        logger.error(f"Speech recognition service error: {e}")
        speak("Нажаль щось пішло не так, спробуйте знову!")


async def process_text(response):
    logger.info(f"User said: {str(response)}")
    base(response)


async def main():
    # Ініціалізація розпізнавача мови
    recognizer = sr.Recognizer()
    # Встановлення порогу паузи (час очікування перед розпізнаванням)
    recognizer.pause_threshold = 0.5
    # Ініціалізація мікрофону
    microphone = sr.Microphone()

    speak("Програма розпочала роботу. Говоріть в мікрофон.")
    logger.info("Program started")

    while True:
        # Виклик асинхронної функції розпізнавання мови з мікрофону
        await recognize_speech_from_mic(recognizer, microphone)


if __name__ == "__main__":
    asyncio.run(main())
